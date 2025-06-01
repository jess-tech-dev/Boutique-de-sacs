document.querySelectorAll('.achat').forEach(button => {
    button.addEventListener('click', () => {
        alert('Achat effectué !');
    });
});

document.querySelectorAll('.panier').forEach(button => {
    button.addEventListener('click', () => {
        alert('Article ajouté au panier !');
    });
});
async function ajouterAuPanier(article) {
    const response = await fetch('/ajouter_panier', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nom: article, prix: 10 })
    });
    const data = await response.json();
    console.log(data);
}

