<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Input Form</title>
</head>
<body>
    <h2>Enter Values for Calculation</h2>
    <form action="process.php" method="get">
        <label for="a">Value of a:</label>
        <input type="number" id="a" name="a" required><br><br>

        <label for="b">Value of b:</label>
        <input type="number" id="b" name="b" required><br><br>

        <label for="c">Value of c:</label>
        <input type="number" id="c" name="c" required><br><br>

        <label for="d">Value of d:</label>
        <input type="number" id="d" name="d" required><br><br>

        <label for="e">Value of e:</label>
        <input type="number" id="e" name="e" required><br><br>

        <input type="submit" value="Calculate">
    </form>
</body>
</html>