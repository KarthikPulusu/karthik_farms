<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $number = $_POST["number"];
    $pincode = $_POST["pincode"];
    
    $to = "kpulusu0@gmail.com";  // Replace with your email address
    $subject = "New Form Submission";
    $headers = "From: $email";
    
    $mailBody = "Name: $name\nNumber: $number\nPincode: $pincode";
    
    if (mail($to, $subject, $mailBody, $headers)) {
        echo "Thank you for your submission!";
    } else {
        echo "Error sending email.";
    }
}
?>
