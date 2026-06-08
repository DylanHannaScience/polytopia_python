from polytopia_score_counter.rewards import calculate_reward
from polytopia_score_counter.actions import _2D_ACTIONS


def main():
    score = 0

    # Loop through each action and calculate the reward
    for action_info in _2D_ACTIONS:
        action = action_info["action"]
        # Call calculate_reward dynamically with the appropriate arguments
        reward = calculate_reward(action, **{key: value for key, value in action_info.items() if key != "action"})
        score += reward
        print(f"Reward for {action}: {reward}")

    print(f'Total score: {score}')


if __name__ == "__main__":
    main()
