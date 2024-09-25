<?php

// Function to verify the signature
function check_signature($raw_webhook_body_path, $signature_path, $key_path) {
    // Read the signature and raw webhook body
    $signature = file_get_contents($signature_path);
    $raw_webhook_body = file_get_contents($raw_webhook_body_path);

    // Split the signature into components (timestamp, version, ubble_signature)
    list($timestamp, $ubble_signature_version, $ubble_signature) = explode(":", $signature);

    // Create the signed payload
    $signed_payload = $timestamp . ":" . $raw_webhook_body;

    // Load the public key
    $public_key = file_get_contents($key_path);

    // Decode the signature from Base64
    $decoded_signature = base64_decode($ubble_signature);

    // Verify the signature using OpenSSL
    $verified = openssl_verify($signed_payload, $decoded_signature, $public_key, OPENSSL_ALGO_SHA512);

    // Check verification result
    if ($verified === 1) {
        echo "Success\n";
    } elseif ($verified === 0) {
        echo "Could not validate signature\n";
    } else {
        echo "Error during signature verification\n";
    }
}

// Command-line arguments handling
if ($argc !== 4) {
    echo "Usage: php index.php <raw_webhook_body_path> <signature_path> <key_path>\n";
    exit(1);
}

// Execute the function with provided arguments
check_signature($argv[1], $argv[2], $argv[3]);

?>

