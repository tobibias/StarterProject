# MIT License
#
# Copyright (c) 2022 Tobias Höfer
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================
"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
from typing import List, Optional

import requests  #type: ignore # pylint: disable=W0611


class MyClass:
    """Summary of class here.

    Longer class information...
    Longer class information...

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam: bool = False):
        """Inits SampleClass with blah."""
        # TODO(yourusername): Rewrite this class.
        self.likes_spam = likes_spam
        self.eggs = 0

    def _internal_function(self):
        # A docstring is mandatory for every function that has one or more of
        # the following properties: being part of the public API,
        # nontrivial size or non-obvious logic.
        _internal_variable = 8  # pylint: disable=C0103, W0612
        pass

    def public_method(
            self,
            word: str = "wuff",
            exclude: Optional[List[str]] = None,
            include_word: bool = False) -> str:  # pylint: disable=W0613
        """Summary of method here.

        Longer method information...
        Longer method information...

        Args:
            word: String to include in result.
            exclude: A list of strings that is jsut a dummy parameter.
            include_word: If True word will be used in result string.

        Returns:
            A dict mapping keys to the corresponding table row data
            fetched. Each row is represented as a tuple of strings. For
            example:

        Raises:
            IOError: An error occurred accessing the smalltable.
        """
        # Use a sentinel value instead of a mutable default value as an
        # argument.
        if exclude is None:
            exclude = ["test"]  # Small explanation.

        return f"{word}"
