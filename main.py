from simplex_method import SimplexMethodSolver, ProblemType, LimitConditionType


def main():
    target = ((3, 2), ProblemType.MAX)
    limit_conditions = (
        (2, 1, LimitConditionType.LE, 20),
        (1, 3, LimitConditionType.LE, 27)
    )
    solver = SimplexMethodSolver(target=target,
                                 limit_conditions=limit_conditions)
    solution = solver.solve()
    print(f'{solution = }')


if __name__ == "__main__":
    main()
