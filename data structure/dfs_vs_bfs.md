Berikut perbandingan alur eksekusi **DFS** dan **BFS** jika dijalankan dengan `start = 2` pada **graph yang sama**:

```python
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)
```

---

### **Perbandingan Eksekusi DFS vs BFS**
| Langkah | **DFS (Depth-First Search)** | **BFS (Breadth-First Search)** |
|---------|----------------------------|----------------------------|
| **1**   | Mulai dari `2`, kunjungi `0` | Mulai dari `2`, enqueue `0` dan `3` |
| **2**   | Dari `0`, kunjungi `1` | Dequeue `2`, cetak `2` |
| **3**   | `1` tidak punya tetangga baru, kembali ke `0` | Dequeue `0`, enqueue `1` |
| **4**   | Kembali ke `2`, kunjungi `3` | Dequeue `3` (tidak enqueue karena sudah dikunjungi) |
| **5**   | `3` hanya terhubung ke dirinya sendiri (sudah dikunjungi), selesai. | Dequeue `1` (tidak enqueue karena sudah dikunjungi), selesai. |

---

### **Urutan Kunjungan**
#### **DFS (rekursif, menyelam dalam)**
```
2 → 0 → 1 → 3
```
#### **BFS (melebar dari start)**
```
2 → 0 → 3 → 1
```

**Kesimpulan:**
- **DFS** menyusuri jalur terdalam sebelum kembali.
- **BFS** menjelajahi semua node di satu level sebelum lanjut ke level berikutnya.