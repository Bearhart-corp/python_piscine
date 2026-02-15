from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def get_class_methods(cls):
    return [name for name, v in cls.__dict__.items()
            if callable(v) and not name.startswith("__")]


def main():
    print("\n=== DataDeck Game Engine ===\n")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    print("Configuring Fantasy Card Game...")
    print(f"Factory: {factory.__class__.__name__}")
    print(f'Strategy name: {strategy.get_strategy_name()}')
    print(f"Available types: {factory.get_supported_types()}")
    print("\nSimulating aggressive turn...")
    result = engine.simulate_turn()
    print("Turn execution:")
    print("Strategy:", strategy.get_strategy_name())
    print("Actions:", result)
    print("\nGame Report:")
    print(engine.get_engine_status())
    print("\nAbstract Factory + Strategy Pattern: \
Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
