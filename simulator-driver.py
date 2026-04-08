from mabwiser.mab import MAB, LearningPolicy
import random

## Whatever you want to define
arms = ["Cards", "Traditional", "Swipe"] # Various UX
jobseeker = [{"id": 1, "age": 1}, {"id": 2, "age": 2}, {"id": 3, "age": 3}] # Example job seeker datas
company = [{"id": 1, "difficulty": 1}, {"id": 2, "difficulty": 1}] # Example company datas
jobs = {1: [{"id": 1, "difficulty": 1}], 2: [{"id": 2, "difficulty": 2}]} # Example job datas
N_RUNS = 1000 # How many runs?
# TODO: Please adjust the decisions and rewards accordingly.
# TODO: ...or you may as well integrate into the driver

linUCB = MAB(arms, LearningPolicy.LinUCB(alpha=1.25)) # Linear UCB, for contextual.
linTS = MAB(arms, LearningPolicy.LinTS(alpha=1.25)) # Linear Thompson Sampling, for contextual.

# TODO: According to your needs, do whatever adjustment you like.
# Take note that this is ONLINE LEARNING!

for e in range(N_RUNS):
    jobseeker_context = random.choice(jobseeker)
    company_context = random.choice(company)
    job_context = random.choice(jobs[company_context["id"]])
    arm = random.choice(arms) # In the future, this will be from the algorithm
    fit_score = jobseeker_context["age"] * company_context["difficulty"] * job_context["difficulty"] # Example fit score, you can adjust this.
    print(f"Job Seeker Context: {jobseeker_context}, Company Context: {company_context}, Job Context: {job_context}")
    print(f"Fit Score: {fit_score}")
    print("Then the arm will be updated in this point")
print("End of simulation.")