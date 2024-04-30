# Memory Game

The app is a memory game where a user can create his or her own packs of cards, each card has a keyword and a definition. The user can use this either for studying or for fun.

## Documentation

[Requirements Definition](./memorygame/src/documentation/RequirementDefinition.md)

[Tuntikirjanpito](./memorygame/src/documentation/tuntikirjanpito.md)

[ChangeLog](./memorygame/src/documentation/changelog.md)

[Architecture Description](./memorygame/src/documentation/arkkitehtuuri.md)

## Release

- [Release - 1](https://github.com/modaralgayal/ohte-modar-2024/releases/tag/release1)

- [Release - 2](https://github.com/modaralgayal/ohte-modar-2024/releases/tag/release2)

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

Run this from the memorygame/ directory

```bash
 poetry run invoke start
```

### Testing

```bash
 poetry run invoke coverage
```

### Testing percentage

```bash
 poetry run invoke coverage-report
```

```bash
 poetry run invoke report
```

### Pylint

```bash
 poetry run invoke lint
```
