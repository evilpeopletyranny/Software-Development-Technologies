from memento import Game, GameSaveManager


def main():
    game = Game()
    save_manager = GameSaveManager()

    # Изменяем состояние игры и сохраняем его
    game.move_player(10)
    game.add_score(50)
    save_manager.save_state(game)

    game.move_player(20)
    game.add_score(30)
    save_manager.save_state(game)

    game.move_player(30)
    game.add_score(20)
    print(f"Current Game State: Position={game.player_position}, Score={game.score}")

    print("\nRestoring to last saved state:")
    save_manager.restore_state(game)
    print(f"Game State after restoration: Position={game.player_position}, Score={game.score}")

    print("\nRestoring to previous saved state:")
    save_manager.restore_state(game)
    print(f"Game State after restoration: Position={game.player_position}, Score={game.score}")

    print("\nAttempting to restore beyond history:")
    save_manager.restore_state(game)


if __name__ == "__main__":
    main()
