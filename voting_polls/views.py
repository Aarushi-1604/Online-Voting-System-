from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll, Candidate, Vote
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError

def ongoing_polls(request):
    polls = Poll.objects.all()  # Retrieve all polls
    return render(request, 'voting_ongoing.html', {'polls': polls})

@login_required
def vote(request, poll_id):
    # Get the poll using poll_id or return 404 if it doesn't exist
    poll = get_object_or_404(Poll, id=poll_id)
    candidates = poll.candidates.all()

    if request.method == 'POST':
        candidate_id = request.POST.get('candidate')
        if not candidate_id:
            return redirect('vote', poll_id=poll_id)
        else:
            print(candidate_id)

        # Get the candidate or raise 404 if invalid
        candidate = get_object_or_404(Candidate, id=candidate_id, poll=poll)

        try:
            # Create a new vote
            Vote.objects.create(user=request.user, candidate=candidate, poll=poll)
            messages.success(request, f"Your vote for {candidate.name} has been recorded!")
        except IntegrityError:
            # Handle duplicate vote attempts
            messages.error(request, "You have already voted in this poll.")

        # Redirect back to the ongoing polls page
        return redirect('ongoing_polls')

    return render(request, 'voting_vote.html', {'poll': poll, 'candidates': candidates})
