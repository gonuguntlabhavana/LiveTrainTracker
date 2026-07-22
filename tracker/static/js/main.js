document.addEventListener("DOMContentLoaded", function () {

    const trainInput = document.getElementById("trainInput");
    const suggestions = document.getElementById("suggestions");

    trainInput.addEventListener("keyup", function () {

        const text = trainInput.value;

        if (text.length == 0) {
            suggestions.innerHTML = "";
            return;
        }

        fetch(`/search/?q=${text}`)
            .then(response => response.json())
            .then(data => {

                suggestions.innerHTML = "";

                data.forEach(train => {

                    suggestions.innerHTML += `
                        <div class="item"
                             onclick="selectTrain('${train.name}')">
                            ${train.number} - ${train.name}
                        </div>
                    `;

                });

            });

    });

});

function selectTrain(name) {

    document.getElementById("trainInput").value = name;

    document.getElementById("suggestions").innerHTML = "";

}
function addFavorite(number, name) {

    fetch(`/favorite/?number=${number}&name=${encodeURIComponent(name)}`)
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        });

}
function showLoading(){

    document.getElementById("loading").style.display = "block";

}