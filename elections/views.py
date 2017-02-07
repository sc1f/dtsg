from django.shortcuts import render
from .models import Election, Race, Candidate


def index(request):
    elections = Election.objects.all().order_by('-year')
    return render(request, 'elections/electionsindex.html', {'Elections': elections})

def election(request, year):
    selected_election = Election.objects.get(year=year)
    races = Race.objects.filter(year=selected_election.year).all()
    return render(request, 'elections/election.html', {'election': selected_election, 'races': races})

def race(request, year, race_id):
    selected_election = Election.objects.get(year=year)
    selected_race = Race.objects.get(id=race_id)

    candidates = Candidate.objects.filter(race_id=race_id)

    return render(request, 'elections/race.html', {
        'election': selected_election,
        'race': selected_race,
        'Candidates': candidates,
        'year': year
    })

def candidate(request, year, race_id, candidate_id):
    selected_election = Election.objects.get(year=year)
    selected_race = Race.objects.get(id=race_id)
    selected_candidate = Candidate.objects.get(id=candidate_id)

    return render(request, 'elections/candidate.html', {
        'election':selected_election,
        'race': selected_race,
        'candidate': selected_candidate
    })
