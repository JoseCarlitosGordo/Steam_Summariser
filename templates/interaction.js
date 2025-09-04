game_btn = document.getElementById("searchBar")


runQuery()

game_btn.addEventListener("click", (e) => 
    {
        runQuery()

})
function runQuery()
{
    let text = document.querySelector(["name = game_name"])

    fetch("/find_game")
    .then(response => response.json())
    .then(data => 
    {
        console.log(data);

    })
}