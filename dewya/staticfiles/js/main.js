// Small helpers (placeholder)
console.log("The Dewy Ritual - scripts loaded");

document.addEventListener("DOMContentLoaded", function () {
    // Scroll Reveal for product cards
    const cards = document.querySelectorAll(".card");
    const revealCards = () => {
        const triggerBottom = window.innerHeight * 0.85;
        cards.forEach(card => {
            const boxTop = card.getBoundingClientRect().top;
            if (boxTop < triggerBottom) {
                card.classList.add("visible");
            }
        });
    };
    window.addEventListener("scroll", revealCards);
    revealCards();
});
