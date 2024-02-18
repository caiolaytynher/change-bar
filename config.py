from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    theme: str
    wallpapers: dict[str, dict[str, Path]]


config = Config(
    theme="onedark",
    wallpapers={
        "gruvbox": {
            "normal": Path.home()
            / "Pictures/wallpapers/alena-aenami-serenity.jpg",
            "vibrant": Path.home()
            / "Themes/Gruvbox-GTK-Theme/wallpapers/gruvbox20.png",
            "utility": Path.home()
            / "Themes/Gruvbox-GTK-Theme/wallpapers/gruvbox20.png",
        },
        "dracula": {
            "normal": Path.home() / "Pictures/wallpapers/blue-landscape.jpg",
            "vibrant": Path.home()
            / "Themes/Dracula-wallpapers/first-collection/"
            "dracula-wallpaper.svg",
            "utility": Path.home()
            / "Themes/Dracula-wallpapers/first-collection/"
            "dracula-wallpaper.svg",
        },
        "catppuccin": {
            "normal": Path.home() / "Pictures/wallpapers/sakura-tree.jpg",
            "vibrant": Path.home() / "Themes/Catppuccin-wallpapers/mandelbrot/"
            "mandelbrot_full_flamingo.png",
            "utility": Path.home() / "Themes/Catppuccin-wallpapers/mandelbrot/"
            "mandelbrot_full_flamingo.png",
        },
        "tokyonight": {
            "normal": Path.home()
            / "Pictures/wallpapers/alena-aenami-the-city-view.jpg",
            "vibrant": Path.home()
            / "Themes/Tokyo-Night-GTK-Theme/wallpapers/tokyo-night31.png",
            "utility": Path.home()
            / "Themes/Tokyo-Night-GTK-Theme/wallpapers/tokyo-night31.png",
        },
        "everforest": {
            "normal": Path.home() / "Pictures/wallpapers/ocean-view-room.jpg",
            "vibrant": Path.home()
            / "Themes/Everforest-GTK-Theme/wallpapers/everforest01.jpg",
            "utility": Path.home()
            / "Themes/Everforest-GTK-Theme/wallpapers/everforest01.jpg",
        },
        "kanagawa": {
            "normal": Path.home() / "Pictures/wallpapers/the-great-wave.jpg",
            "vibrant": Path.home()
            / "Pictures/wallpapers/the-great-wave-minimal.png",
            "utility": Path.home()
            / "Pictures/wallpapers/the-great-wave-minimal.png",
        },
        "onedark": {
            "normal": Path.home()
            / "Pictures/wallpapers/sebastian-luca-flooded-cathedral.jpg",
            "vibrant": Path.home() / "Themes/OneDarkWallpapers/34.png",
            "utility": Path.home() / "Themes/OneDarkWallpapers/34.png",
        },
    },
)
