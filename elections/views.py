from django.shortcuts import render
from .models import Election, Race, Candidate


def index(request):
    elections = Election.objects.all()
    return render(request, 'elections/index.html', {'Elections': elections})

def election(request, year):
    selected_election = Election.objects.get(year=year)
    races = Race.objects.filter(year_id=selected_election.id).all()
    return render(request, 'elections/election.html', {'election': selected_election, 'races': races})

def race(request, year, race_id):
    selected_race = Race.objects.get(id=race_id)

    candidates = Candidate.objects.filter(race_id=race_id)

    return render(request, 'elections/race.html', {
        'race': selected_race,
        'Candidates': candidates,
        'year': year
    })

def candidate(request, year, race_id, candidate_id):
    selected_race = Race.objects.get(id=race_id)
    selected_candidate = Candidate.objects.get(id=candidate_id)

    return render(request, 'elections/candidate.html', {'race': selected_race, 'candidate': selected_candidate})
