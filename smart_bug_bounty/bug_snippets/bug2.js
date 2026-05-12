/**
 * Bir dizideki sayıların toplamını hesaplayan fonksiyon.
 * for...in kullanımı nedeniyle hatalı sonuç verebilir.
 */
function calculateSum(numbers) {
    let total = 0;
    
    // BUG: Dizilerde 'in' kullanmak değerleri değil indeksleri (string olarak) getirir
    // Bu da toplama yerine yan yana birleştirme (concatenation) yapabilir.
    for (let index in numbers) {
        total += numbers[index];
    }
    
    return total;
}

const prices = [100, 200, 300];
console.log("Toplam Fiyat:", calculateSum(prices));
