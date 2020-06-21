import pytest

class Tests:

  def test_for_loop_version(self, capsys, monkeypatch):
    """
    Checks whether the output is correct using a for loop.
    """

    from for_loop_version import sing

    # run the function
    sing(5)

    # expected output
    expected = """
5 bottles of beer on the wall, 5 bottles of beer.
Take one down, pass it around, 4 bottles of beer on the wall.

4 bottles of beer on the wall, 4 bottles of beer.
Take one down, pass it around, 3 bottles of beer on the wall. 

3 bottles of beer on the wall, 3 bottles of beer.
Take one down, pass it around, 2 bottles of beer on the wall.

2 bottles of beer on the wall, 2 bottles of beer.
Take one down, pass it around, 1 bottle of beer on the wall.

1 bottle of beer on the wall, 1 bottle of beer.
Take it down, pass it around, no more bottles of beer on the wall!
    """.strip()
    
    # get the output
    captured = capsys.readouterr()  # capture print output
    actual = captured.out.lower().strip()  # remove leading/trailing whitespace

    # remove multiple whitespaces
    actual = ' '.join(actual.split())
    expected = ' '.join(expected.split())

    # make sure the program only asked for input until a valid one was given
    assert actual.lower() == expected.lower()

  def test_while_loop_accumulator_version(self, capsys, monkeypatch):
    """
    Checks whether the output is correct using a while loop with accumulator
    """

    from while_loop_accumulator_version import sing
    
    # run the function
    sing(5)

    # expected output
    expected = """
5 bottles of beer on the wall, 5 bottles of beer.
Take one down, pass it around, 4 bottles of beer on the wall.

4 bottles of beer on the wall, 4 bottles of beer.
Take one down, pass it around, 3 bottles of beer on the wall. 

3 bottles of beer on the wall, 3 bottles of beer.
Take one down, pass it around, 2 bottles of beer on the wall.

2 bottles of beer on the wall, 2 bottles of beer.
Take one down, pass it around, 1 bottle of beer on the wall.

1 bottle of beer on the wall, 1 bottle of beer.
Take it down, pass it around, no more bottles of beer on the wall!
    """.strip()
    
    # get the output
    captured = capsys.readouterr()  # capture print output
    actual = captured.out.lower().strip()  # remove leading/trailing whitespace

    # remove multiple whitespaces
    actual = ' '.join(actual.split())
    expected = ' '.join(expected.split())

    # make sure the program only asked for input until a valid one was given
    assert actual.lower() == expected.lower()

  def test_while_loop_flag_version(self, capsys, monkeypatch):
    """
    Checks whether the output is correct using a while loop with accumulator
    """

    from while_loop_flag_version import sing
    
    # run the function
    sing(5)

    # expected output
    expected = """
5 bottles of beer on the wall, 5 bottles of beer.
Take one down, pass it around, 4 bottles of beer on the wall.

4 bottles of beer on the wall, 4 bottles of beer.
Take one down, pass it around, 3 bottles of beer on the wall. 

3 bottles of beer on the wall, 3 bottles of beer.
Take one down, pass it around, 2 bottles of beer on the wall.

2 bottles of beer on the wall, 2 bottles of beer.
Take one down, pass it around, 1 bottle of beer on the wall.

1 bottle of beer on the wall, 1 bottle of beer.
Take it down, pass it around, no more bottles of beer on the wall!
    """.strip()
    
    # get the output
    captured = capsys.readouterr()  # capture print output
    actual = captured.out.lower().strip()  # remove leading/trailing whitespace

    # remove multiple whitespaces
    actual = ' '.join(actual.split())
    expected = ' '.join(expected.split())

    # make sure the program only asked for input until a valid one was given
    assert actual.lower() == expected.lower()
