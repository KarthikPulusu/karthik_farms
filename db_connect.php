<?php
// Database connection settings
$servername = "localhost";
$username = "karthik";
$password = "karthik@007";
$dbname = "karthikfarms";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $number = $_POST['number'];
    $address = $_POST['address'];
    $pincode = $_POST['pincode'];
    $gender = $_POST['gender'];
    $item = $_POST['item'];
    $quantity = $_POST['quantity'];
    $transaction_id = $_POST['transaction_id'];

    // SQL query to insert data into the 'orders' table
    $stmt = $conn->prepare("INSERT INTO orders (name, number, address, pincode, gender, item, quantity, transaction_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("sissssss", $name, $number, $address, $pincode, $gender, $item, $quantity, $transaction_id);
    //$sql = "INSERT INTO orders (name, number, address, pincode, gender, item, quantity, transaction_id) 
      //      VALUES ('$name', '$number', '$address', '$pincode', '$gender', '$item', '$quantity', '$transaction_id')";

    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        http_response_code(405);
        echo "Method Not Allowed";
        //echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

// Close the connection
$conn->close();
?>
