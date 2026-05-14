const books = [
    {
        title: "The Alchemist",
        author: "Paulo Coelho",
        price: 450
    },
    {
        title: "To Kill a Mockingbird",
        author: "Harper Lee",
        price: 550
    },
    {
        title: "Atomic Habits",
        author: "James Clear",
        price: 600
    }
];

// Display Books
function displayBooks(bookArray) {

    const bookList = document.getElementById("bookList");

    bookList.innerHTML = "";

    bookArray.forEach(book => {

        bookList.innerHTML += `
            <div class="book">
                <h3>${book.title}</h3>
                <p><strong>Author:</strong> ${book.author}</p>
                <p><strong>Price:</strong> ₹${book.price}</p>
            </div>
        `;
    });
}

// Search Books
function searchBooks() {

    const searchText = document
        .getElementById("search")
        .value
        .toLowerCase();

    const filteredBooks = books.filter(book =>
        book.title.toLowerCase().includes(searchText) ||
        book.author.toLowerCase().includes(searchText)
    );

    displayBooks(filteredBooks);
}

// Initial Display
displayBooks(books);