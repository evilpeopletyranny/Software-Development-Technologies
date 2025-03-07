class GameState:
    def __init__(self, player_position: int, score: int) -> None:
        self.player_position = player_position
        self.score = score

    def __repr__(self) -> str:
        return f"GameState(Position={self.player_position}, Score={self.score})"


class Game:
    def __init__(self) -> None:
        self.player_position = 0
        self.score = 0

    def move_player(self, new_position: int) -> None:
        self.player_position = new_position
        print(f"Player moved to position: {self.player_position}")

    def add_score(self, points: int) -> None:
        self.score += points
        print(f"Score increased by {points}. Current score: {self.score}")

    def save(self) -> GameState:
        print(f"Saving game state: Position={self.player_position}, Score={self.score}")
        return GameState(self.player_position, self.score)

    def restore(self, state: GameState) -> None:
        self.player_position = state.player_position
        self.score = state.score
        print(f"Game state restored: Position={self.player_position}, Score={self.score}")


class GameSaveManager:
    def __init__(self) -> None:
        self.save_stack = []

    def save_state(self, game: Game) -> None:
        self.save_stack.append(game.save())

    def restore_state(self, game: Game) -> None:
        if self.save_stack:
            state = self.save_stack.pop()
            game.restore(state)
        else:
            print("No saved states to restore.")