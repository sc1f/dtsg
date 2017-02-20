from django.shortcuts import render
from django.db.models import Count
from .models import Election, Race, Position
from .forms import CandidateForm

def election_index(request):
    elections = Election.objects.all().order_by('-year')
    return render(request, 'elections/elections_index.html', {
        'Elections': elections
    })

def races(request, year):
    selected_election = Election.objects.get(year=year)
    races = Race.objects.filter(year=selected_election.year).all().annotate(num_positions=Count('position'))

    return render(request, 'elections/races.html', {
        'election': selected_election,
        'races': races
    })

def positions(request, year, race_id):
    selected_election = Election.objects.get(year=year)
    selected_race = Race.objects.get(id=race_id)
    positions = selected_race.position_set.all().filter(candidate__published=True).annotate(num_candidates=Count('candidate')).order_by('order')
    positions_count = selected_race.position_set.all().count()

    return render(request, 'elections/positions.html', {
        'election': selected_election,
        'race': selected_race,
        'Positions': positions,
        'positions_count': positions_count,
        'year': year
    })

def candidates(request, year, race_id, position_id):
    selected_position = Position.objects.get(id=position_id)
    selected_election = Election.objects.get(year=year)
    selected_race = Race.objects.get(id=race_id)

    candidates = selected_position.candidate_set.filter(published=True).order_by('name')
    candidates_count = candidates.count()

    # TODO validate counts


    return render(request, 'elections/candidates.html', {
        'year': year,
        'election':selected_election,
        'race': selected_race,
        'position': selected_position,
        'Candidates': candidates,
        'candidates_count': candidates_count
    })

def add_candidate(request, year):
    if request.POST:
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            cand = form.save(commit=False)
            cand.winner = False
            cand.save()
            return render(request,'elections/survey_submitsuccess.html',{})
        else:
            err = form.errors.as_data()
            return render(request, 'elections/survey.html', {'form': form, 'year': year, 'error': err})
    else:
        form = CandidateForm()
        #form.fields['position'].queryset = Position.objects.filter(race_id = form.fields['race'].id)
        return render(request, 'elections/survey.html', {'form': form, 'year': year})
