class InfoMessage:
    """Training information message."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        return (f'Type of workout: {self.training_type}; '
                f'Duration: {self.duration:.3f} h.; '
                f'Distance: {self.distance:.3f} km.; '
                f'Mean speed: {self.speed:.3f} km/h; '
                f'Kcal spent: {self.calories:.3f}.')


class Training:
    """Basic training class."""
    M_IN_KM = 1000
    LEN_STEP = 0.65
    HOUR_TO_MIN = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Get the distance in km."""
        return (self.action * self.LEN_STEP) / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Get the average driving speed."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Get the number of calories burned."""
        return 0

    def show_training_info(self) -> InfoMessage:
        """Return an information message about the completed workout."""
        return InfoMessage(self.__class__.__name__, self.duration,
                           self.get_distance(), self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Training: running."""
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def get_spent_calories(self):
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed()
                 + self.CALORIES_MEAN_SPEED_SHIFT) * self.weight / self.M_IN_KM
                * self.duration * self.HOUR_TO_MIN)


class SportsWalking(Training):
    """Training: race walking."""
    K_1 = 0.035
    K_2 = 0.029
    TO_MET_SEC = 0.278
    TO_MET_FROM_SM = 100

    def __init__(self, action, duration, weight, height):
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self):
        return ((self.K_1 * self.weight
                + ((self.get_mean_speed() * self.TO_MET_SEC) ** 2
                 / (self.height / self.TO_MET_FROM_SM)) * self.K_2
                * self.weight) * self.duration * self.HOUR_TO_MIN)


class Swimming(Training):
    """Training: swimming."""
    LEN_STEP = 1.38
    MEAN_SPEED_DIFF = 1.1
    SPEED_MULT = 2

    def __init__(self, action, duration, weight, length_pool, count_pool):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self):
        return (self.length_pool * self.count_pool / self.M_IN_KM
                / self.duration)

    def get_spent_calories(self):
        return ((self.get_mean_speed() + self.MEAN_SPEED_DIFF)
                * self.SPEED_MULT * self.weight * self.duration)


def read_package(workout_type: str, data: list) -> Training:
    """Read data received from sensors."""
    train = {'SWM': Swimming,
             'RUN': Running,
             'WLK': SportsWalking}

    return train[workout_type](*data)


def main(training: Training) -> None:
    """Main function."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180])
    ]

    for workout_type, data in packages:
        print(type(workout_type), type(data))
        training = read_package(workout_type, data)
        main(training)
