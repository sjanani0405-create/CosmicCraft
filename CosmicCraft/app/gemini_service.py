from .schemas import ComicResponse


def generate_comic(request):
    idea = request.prompt.lower()

    panels = [
        {
            "panel_number": 1,
            "scene": (
                "Alex explores an abandoned space station and discovers "
                "a mysterious glowing robot hidden inside a control room."
            ),
            "dialogue": (
                "Alex: Who are you? And why are you glowing?"
            ),
            "caption": (
                "A strange discovery begins an incredible adventure."
            ),
            "image_prompt": (
                "Colorful cartoon comic scene inside an abandoned space "
                "station. A young inventor discovers a small friendly "
                "glowing robot."
            )
        },
        {
            "panel_number": 2,
            "scene": (
                "Robo projects a holographic star map showing a hidden "
                "planet far beyond the known galaxies."
            ),
            "dialogue": (
                "Robo: This map leads to a planet containing an ancient "
                "cosmic library."
            ),
            "caption": (
                "The mysterious robot reveals the secret destination."
            ),
            "image_prompt": (
                "Colorful cartoon comic scene with a friendly robot "
                "projecting a glowing holographic star map in space."
            )
        },
        {
            "panel_number": 3,
            "scene": (
                "Alex and Robo travel through colorful galaxies in a "
                "small spacecraft while following the holographic map."
            ),
            "dialogue": (
                "Alex: Look at those galaxies! We must be getting close."
            ),
            "caption": (
                "The journey takes them across the colorful universe."
            ),
            "image_prompt": (
                "Bright colorful cartoon comic scene of a small spacecraft "
                "traveling through beautiful galaxies, stars and planets."
            )
        },
        {
            "panel_number": 4,
            "scene": (
                "The spacecraft reaches the hidden planet. Alex and Robo "
                "discover a gigantic ancient cosmic library."
            ),
            "dialogue": (
                "Alex: I've never seen anything this amazing!"
            ),
            "caption": (
                "The legendary cosmic library has finally been found."
            ),
            "image_prompt": (
                "Epic colorful cartoon comic scene showing a huge ancient "
                "cosmic library on a mysterious alien planet."
            )
        },
        {
            "panel_number": 5,
            "scene": (
                "Inside the library, Alex discovers that its protective "
                "energy shield is disappearing. A puzzle appears on an "
                "ancient glowing doorway."
            ),
            "dialogue": (
                "Robo: We have to solve the puzzle before the library "
                "loses its protection!"
            ),
            "caption": (
                "The explorers must solve the ancient puzzle."
            ),
            "image_prompt": (
                "Colorful cartoon comic scene inside a magical cosmic "
                "library. A young inventor and friendly robot examine "
                "a glowing ancient puzzle."
            )
        },
        {
            "panel_number": 6,
            "scene": (
                "Alex solves the puzzle and the library lights up with "
                "thousands of stars. The ancient knowledge is safe."
            ),
            "dialogue": (
                "Alex: We did it! The cosmic library is safe!"
            ),
            "caption": (
                "Alex and Robo become guardians of the incredible library."
            ),
            "image_prompt": (
                "Happy colorful cartoon comic ending. A young inventor "
                "and friendly robot stand inside a glowing cosmic library "
                "filled with stars and magical books."
            )
        }
    ]

    # Use the requested number of panels.
    panels = panels[:request.panel_count]

    return ComicResponse(
        title="The Cosmic Adventure",
        characters=[
            {
                "name": "Alex",
                "description": (
                    "A curious young inventor who loves exploring "
                    "mysterious places."
                )
            },
            {
                "name": "Robo",
                "description": (
                    "A friendly glowing robot who knows the secrets "
                    "of the universe."
                )
            }
        ],
        panels=panels
    )
