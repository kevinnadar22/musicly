# Music Player Architecture

## Overview
The music player has been refactored into a clean, maintainable architecture with clear separation of concerns.

## Structure

### 1. **Entry Point** (`player/main.py`)
- CLI entry point, No business logic,
- Usage: `musicly "song name"` or just `musicly` to open empty player

### 2. **GUI Layer** (`player/gui/player.py`)
- Handles all UI interactions and display updates
- No direct access to download/playback utilities

### 3. **Service Layer** (`player/gui/player_service.py`)
- Business logic for music player operations
- Handles:
  - Song search and download (threaded)
  - Audio playback management
  - FFmpeg installation if needed
- Isolated from GUI code

### 4. **Utilities** (`player/utils/`)
- `download.py`: YT-DLP audio downloading
- `ffmpeg.py`: FFmpeg installation and management
- `file_operations.py`: File system operations
- `url_helpers.py`: URL and download helpers

## Flow

### Starting with a song name:
```
musicly "Bohemian Rhapsody"
  ↓
main.py calls run_player(song_name="Bohemian Rhapsody")
  ↓
GUI launches and automatically calls PlayerService.search_and_download()
  ↓
Service downloads in background, calls GUI callbacks for progress
  ↓
On complete, Service calls PlayerService.load_and_play()
  ↓
GUI updates display and shows playback controls
```

### Starting without a song:
```
musicly
  ↓
main.py calls run_player(song_name=None)
  ↓
GUI launches with empty state
  ↓
User searches for song via input field
  ↓
[Same flow as above]
```

## Key Features

### Clean Separation
- GUI code never directly calls utilities
- All business logic in PlayerService
- This is easy to maintain

### Threaded Operations
- Downloads happen in background threads
- Callbacks update UI thread-safely

### Error Handling
- Download errors shown in GUI
- FFmpeg auto-installation with progress updates

### State Management
- All player state in PlayerService
- GUI only manages display state

## Usage Examples

### Command Line
```bash
# Play a specific song
musicly "All the stars"

# Open player to search
musicly
```

### Keyboard Controls
- `Space`: Play/Pause
- `s`: Focus search input
- `q`: Quit


## Extension Points

To add new features:

1. **Add to PlayerService** - New playback features (seek, volume, etc.)
2. **Update GUI** - New UI controls or displays
3. **Keep them separate** - Service calls GUI callbacks, GUI calls service methods

## File Organization

```
player/
├── main.py              # CLI entry point
├── config.py            # Configuration
├── gui/
│   ├── __init__.py      # Package exports
│   ├── player.py        # GUI implementation
│   ├── player_service.py # Business logic
│   └── gui.tcss         # Styling
└── utils/
    ├── download.py      # Download logic
    ├── ffmpeg.py        # FFmpeg management
    ├── file_operations.py
    └── url_helpers.py
```
