
using System;
using System.IO;

class FileLoader {
    public void ReadMyFile(string path) {
        Console.WriteLine("Dosya okunuyor: " + path);

        // BUG: StreamReader objesi kapatılmıyor (Close/Dispose yok)
        // Bu durum bellek sızıntısına ve dosyanın kilitli kalmasına yol açar.
        StreamReader reader = new StreamReader(path);
        string data = reader.ReadToEnd();
        
        Console.WriteLine("Veri Okundu. Uzunluk: " + data.Length);
        // reader.Close(); eksik
    }
}
