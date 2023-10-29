window.onload = function() {
            populateCategories();
        }

function filterByCategory() {
    const selectedCategory = document.getElementById('categoryFilter').value;
    const query = document.getElementById('searchBar').value;
    refreshProducts(query, selectedCategory);
}

function searchProducts() {
            const query = document.getElementById('searchBar').value;
            refreshProducts(query);
        }

         async function refreshProducts(query = '', category = '', sort = '') {
        document.getElementById("product_cards").innerHTML = "";
        const products = await getProducts(query, category, sort);
        displayProducts(products);
    }

function displayProducts(products) {
    const container = document.getElementById("product_cards");

    products.forEach((item) => {
        const card = document.createElement('div');
        card.className = 'card';

        // Membuat elemen <a> untuk mengarahkan ke halaman detail buku
        const link = document.createElement('a');
        link.href = `/books/${item.pk}/`;  // Asumsi bahwa URL mengikuti pola /book/<book_id>/
        link.style.textDecoration = 'none';  // Menghapus underline dari link
        link.style.color = 'inherit';  // Warna teks menjadi sama seperti teks lainnya

        // Mengisi konten kartu buku
        link.innerHTML = `
            <h3>${item.fields.title}</h3>
            <p><strong>Author:</strong> ${item.fields.author}</p>
            <p><strong>Publish Date:</strong> ${item.fields.publish_date}</p>
            <p><strong>Rating:</strong> ${item.fields.rating}</p>
        `;


        // Menambahkan link ke kartu dan kartu ke container
        card.appendChild(link);
        container.appendChild(card);
    });
}

function sortProducts() {
            const sortSelect = document.getElementById('sortRating');
            let sortValue = sortSelect.value;
            let sortParam = ''; // Default as title

            if (sortValue === 'desc') {
                sortParam = 'rating'; // If we want to sort by rating in descending order
            } else if (sortValue === 'asc') {
                sortParam = 'rating_asc'; // If we want to sort by rating in ascending order
            }

            refreshProducts('', '', sortParam);
        }