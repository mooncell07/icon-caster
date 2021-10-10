import argparse
import logging
import time
import typing
from dataclasses import dataclass

from PIL import Image

__all__ = ("CLIHandler", "Args", "Caster")


@dataclass
class Args:
    """
    A dataclss representing an Args.

    The instance of this class is taken by Caster to generate the icons.
    """

    filepath: str
    targetpath: str
    imagesize: typing.Optional[typing.List[int]]
    view: bool


class CLIHandler:
    """
    A class representing a CLIHandler.

    This object takes args from the Command Line.
    """

    __slots__ = ("parser",)

    def __init__(self) -> None:
        """
        CLIHandler constructor.
        """
        self.parser: argparse.ArgumentParser = argparse.ArgumentParser(
            description="Takes any image format and converts it to .ico format."
        )

    def accept_args(self) -> None:
        """
        Accepts all the args from Command Line.
        """
        self.parser.add_argument(
            "-F", "--filepath", help="Absolute file path to the image."
        )
        self.parser.add_argument(
            "-T",
            "--targetpath",
            help="Absolute location where the processed image should be saved. (Must end with .ico)",
            default="./image.ico",
        )
        self.parser.add_argument(
            "-S",
            "--imagesize",
            nargs="+",
            type=int,
            help="Size of processed image. Pass 2 dimensions.",
            default=None,
        )

        self.parser.add_argument(
            "-V",
            "--view",
            help="Whether to show the generated icon or no.",
            action="store_true",
        )

    def extract_args(self) -> argparse.Namespace:
        """
        Parses all the args and forms a Namespace.
        """
        return self.parser.parse_args()


class Caster:
    """
    A class representing a Caster.

    This object supports input from any source as long as its getting a valid Args object.
    """

    __slots__ = ("args",)

    def __init__(self, args: Args) -> None:
        """
        Caster Constructor.
        """
        self.args = args

    def get_file(self, file=None) -> typing.Any:
        """
        Opens the image file residing at the filepath.
        """
        try:
            return Image.open(file or self.args.filepath)
        except (FileNotFoundError, AttributeError) as e:
            logging.error(e)

    def generate(self) -> str:
        """
        .ico file generator with also support for viewing the image.
        """
        if isinstance(self.args.imagesize, list):
            imgsize = tuple(self.args.imagesize)
        else:
            imgsize = (255, 255)

        img = self.get_file()
        target = self.args.targetpath

        if img is not None:

            try:
                img.save(target, sizes=[imgsize])
            except ValueError as e:
                logging.error(f"Couldn't save image at: {target}")

            saved_at = self.get_file(target)

            if self.args.view:
                saved_at.show()

            return saved_at.filename


def main() -> str:
    """
    Driver function.
    """
    then = time.time()

    hldr = CLIHandler()

    hldr.accept_args()

    print(f"Started Generation.")
    args = Args(**hldr.extract_args().__dict__)
    print(f"Acquired Args: {args}.")

    cast = Caster(args=args)

    saved = cast.generate()

    if saved is not None:
        print(f"Generated in {time.time() - then}s and saved at {saved}")


if __name__ == "__main__":
    main()
