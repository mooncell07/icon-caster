import argparse
import typing as t
from PIL import Image

__all__ = ("CasterParser",)


class CasterParser(argparse.ArgumentParser):
    """
    A `argparse.ArgumentParser` subclass that can be used to generate icons.
    """

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """
        CasterParser constructor.

        Args:
            *args: Arguments to be passed to the parent class.
            **kwargs: Keyword arguments to be passed to the parent class.
        """
        super().__init__(*args, **kwargs)
        self._args: t.Optional[argparse.Namespace] = None

    def recv(self) -> None:
        """
        A method for receiving arguments from the command line.
        """
        self.add_argument("FILEPATH", help="Location to the image.")
        self.add_argument(
            "TARGETPATH", help="Location where the processed image is to be saved."
        )
        self.add_argument(
            "-D",
            "--DIMENSIONS",
            help="Dimensions of the processed image.",
            nargs="+",
            type=int,
            default=None,
        )
        self.add_argument(
            "-V",
            "--VIEW",
            help="Whether to show the generated icon or no.",
            action="store_true",
        )

    @property
    def args(self) -> argparse.Namespace:
        """
        A property for accessing the arguments.

        Returns:
            argparse.Namespace: The arguments.

        This property is writable so you can pass your own `argparse.Namespace`.
        """
        if self._args is None:
            self._args = self.parse_args()
        return self._args

    @args.setter
    def args(self, value: argparse.Namespace) -> None:
        self._args = value

    def get_file(self, open_target: bool = False) -> Image:
        """
        Gets the file from the FILEPATH argument and opens it.

        Args:
            open_target (bool): Whether to open the target file or not.

        Returns:
            Image: The image.
        """
        return Image.open(self.args.TARGETPATH if open_target else self.args.FILEPATH)

    def generate(self) -> None:
        """
        Generates the icon.
        """
        args = self.args
        file = self.get_file()

        if args.DIMENSIONS is None:
            file.save(args.TARGETPATH)

        else:
            sizes = [(dim, dim) for dim in args.DIMENSIONS]
            file.save(args.TARGETPATH, sizes=sizes)

    def show(self) -> None:
        """
        Shows the icon.
        This method must be called after `generate()` and the generated image must be saved.
        """
        file = self.get_file(open_target=True)
        file.show()


if __name__ == "__main__":
    parser = CasterParser(description="A tool for converting images to icon format.")
    parser.recv()

    parser.generate()
    if parser.args.VIEW:
        parser.show()
