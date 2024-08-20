import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.KeyFactory;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.X509EncodedKeySpec;
import java.util.Base64;

public class CheckWebhookSignature {

    public static void main(String[] args) {
        if (args.length != 3) {
            System.out.println("Usage: java CheckWebhookSignature <rawWebhookBodyPath> <signaturePath> <keyPath>");
            return;
        }

        String rawWebhookBodyPath = args[0];
        String signaturePath = args[1];
        String keyPath = args[2];

        try {
            String signature = Files.readString(Paths.get(signaturePath));
            String rawWebhookBody = Files.readString(Paths.get(rawWebhookBodyPath));
            String[] signatureParts = signature.split(":");

            String timestamp = signatureParts[0];
            // int ubbleSignatureVersion = Integer.parseInt(signatureParts[1]);
            String ubbleSignature = signatureParts[2];

            // First we create the signedPayload
            String signedPayload = timestamp + ":" + rawWebhookBody;
            byte[] signedPayloadBytes = signedPayload.getBytes("UTF-8");

            // Use the public key from the dashboard (check version from ubbleSignatureVersion)
            String publicKeyString = new String(Files.readAllBytes(Paths.get(keyPath)), Charset.defaultCharset());
            String cleanedPublicKeyString = publicKeyString
                .replace("-----BEGIN PUBLIC KEY-----", "")
                .replaceAll(System.lineSeparator(), "")
                .replace("-----END PUBLIC KEY-----", "");
            byte[] publicKeyBytes = Base64.getDecoder().decode(cleanedPublicKeyString);
            X509EncodedKeySpec keySpec = new X509EncodedKeySpec(publicKeyBytes);
            KeyFactory keyFactory = KeyFactory.getInstance("EC");
            PublicKey publicKey = keyFactory.generatePublic(keySpec);

            // Verify the signature
            Signature verifier = Signature.getInstance("SHA512withECDSA");
            verifier.initVerify(publicKey);
            verifier.update(signedPayloadBytes);
            boolean result = verifier.verify(Base64.getDecoder().decode(ubbleSignature));
            if (result) {
                System.out.println("Success");
            } else {
                System.out.println("Could not validate signature");
            }
        } catch (IOException e) {
            System.out.println("An error occurred while reading files: " + e.getMessage());
            e.printStackTrace();
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
