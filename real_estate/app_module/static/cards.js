function getQueryParams() {
    const params = new URLSearchParams(window.location.search);
    return {
        builder: params.get("builder"),
        bhk: params.get("bhk"),
        category: params.get("category")
    };
}

function getPageType() {
    const path = window.location.pathname;

    if (path.includes("/flats/")) return "builder";
    if (path.includes("/rental/")) return "rental";
    if (path.includes("/resale/")) return "resale";


    return null;
}

function getApiUrl() {
    const { builder, bhk, category } = getQueryParams();
    const pageType = getPageType();

    if (pageType === "builder" && builder && bhk) {
        return `http://127.0.0.1:8000/api/flats/?builder__name=${encodeURIComponent(builder)}&category__name=${encodeURIComponent(bhk)}`;
    }

    if (pageType === "rental" && category) {
        return `http://127.0.0.1:8000/api/rent/?category__name=${encodeURIComponent(category)}`;
    }

    if (pageType === "resale" && category) {
        return `http://127.0.0.1:8000/api/resale/?category__name=${encodeURIComponent(category)}`;
    }

    return null;
}

function setTitle() {
    const { builder, bhk, category } = getQueryParams();
    const pageType = getPageType();
    const title = document.getElementById("title");

    if (pageType === "builder") {
        title.innerText = `${builder} - ${bhk} Flats`;
    } else {
        title.innerText = `${category} Flats`;
    }
}


function renderFlats(data) {
    const container = document.getElementById("flatsContainer");
    container.innerHTML = "";

    const pageType = getPageType();   // 🔥 important

    data.forEach(flat => {
        const card = document.createElement("div");
        card.className = "flat-card";

        let priceText = "";
        let extraSection = "";

        // ===== BUILDER FLATS PAGE =====
        if (pageType === "builder") {
            priceText = `₹ ${flat.price}`;

            extraSection = `
                <div class="amenities">
                    <span>Club</span>
                    <span>Football Court</span>
                    <span>Library</span>
                    <span>Malls</span>
                </div>
            `;
        }

        // ===== RENTAL PAGE =====
        if (pageType === "rental") {
            priceText = `Rent: ₹ ${flat.monthly_rent}`;

            extraSection = `
                <p>Deposit: ₹ ${flat.deposit}</p>
                <p>Furnishing: ${flat.furnishing}</p>
            `;
        }

        // ===== RESALE PAGE =====
        if (pageType === "resale") {
            priceText = `₹ ${flat.price}`;

            extraSection = `
                <p>Property Age: ${flat.property_age} years</p>
                <p>Floor: ${flat.floor}</p>
            `;
        }

        card.innerHTML = `
            <img src="${flat.image}" alt="">
            <div class="flat-info">
                <h3>${flat.title}</h3>
                <p>${flat.description}</p>
                <div class="price">${priceText}</div>
                ${extraSection}
            </div>
        `;

        card.addEventListener("click", () => openWhatsApp(flat));
        container.appendChild(card);
    });
}



function openWhatsApp(flat) {
    const builder = flat.builder?.name || "N/A";
    const category = flat.category?.name || "N/A";
    const price = flat.price || "";

    const message = encodeURIComponent(
`Hi, I am interested in this property.

Builder: ${builder}
Category: ${category}
Price: ${price}

Please share more details.`
    );

    const phoneNumber = "918369692520";
    window.open(`https://wa.me/${phoneNumber}?text=${message}`, '_blank');
}



function loadFlats(){
    const apiUrl = getApiUrl();
    console.log("API:", apiUrl);

    if(!apiUrl) return;

    fetch(apiUrl)
        .then(res => res.json())
        .then(data => renderFlats(data));
}

document.addEventListener("DOMContentLoaded", () => {
    setTitle();
    loadFlats();
}

);

// this css for flat_details.html
