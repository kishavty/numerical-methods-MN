def epsilon():
    epsilon = 1

    while (1.0 + epsilon) > 1:
        epsilon /= 2

    return epsilon

epsilon = epsilon()
print(f"Dokładność maszynowa to: {epsilon}")