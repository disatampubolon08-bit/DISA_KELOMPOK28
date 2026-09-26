public class Modul4_Kel28 {
    static void penjumlahan (int a, int b) {
        int c  = a + b;
        System.out.println("Hasil penjumlahan adalah = " +c);
    }
    static void pengurangan () {
        int c = 10 - 20;
        System.out.println("Hasil pengurangan adalah = " +c);
    }
    static int pembagian (int a, int b) {
        int c = a / b;
        return c;
    }
    static int perkalian () {
        int c = 10 * 20;
        return c;
    }
    public static void main(String [] args) {
        penjumlahan(10, 20);

        pengurangan ();

        System.out.println("Hasil perkalian adalah = "+ perkalian());

        int d = pembagian (100, 20);
        System.out.println("Hasil pembagian adalah = "+ d);
    }
}