public class PasswordChecker {
    public static void main(String[] args) {
        // İki farklı String objesi oluşturuluyor
        String storedPass = new String("secure123");
        String enteredPass = new String("secure123");

        System.out.println("Şifre kontrol ediliyor...");

        // BUG: İçerik karşılaştırmak için .equals() yerine == kullanılıyor
        // Bu, değerleri değil bellekteki adresleri karşılaştırır.
        if (enteredPass == storedPass) {
            System.out.println("Giriş Başarılı!");
        } else {
            System.out.println("Hatalı Şifre: Referanslar uyuşmuyor.");
        }
    }
}
