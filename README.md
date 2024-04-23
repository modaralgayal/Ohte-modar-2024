# Memory Game

The app is a memory game where a user can create his or her own packs of cards, each card has a keyword and a definition. The user can use this either for studying or for fun.

## Documentation

[Requirements Definition](./memorygame/RequirementDefinition.md)

[Tuntikirjanpito](./memorygame/tuntikirjanpito.md)

[ChangeLog](./changelog.md)

[Architecture Description](./memorygame/game_sequence.md)

## Download Instructions

1. Download dependencies:

   ```bash
   poetry install
   ```

2. Start the app:

   ```bash
   poetry run invoke start
   ```

## Terminal Commands

### Starting application

    poetry run invoke start

### Testing

    poetry run invoke coverage

### Testing percentage

    poetry run invoke coverage-report

    poetry run invoke report

### Pylint

    poetry run invoke lint
