function main() {
  let refresher = setInterval(refresh, 500)
  let button = document.querySelector(".start-button")
  button.addEventListener("click", () => {
    setTimeout(() => {
      clearInterval(refresher)
    }, 2000)
  })
}

function refresh() {
  let dataDiv = document.querySelector(".room-info")
  let id = dataDiv.dataset.id
  fetch(`/room/${id}/info`)
    .then(response => response.json())
    .then(data => {
      document.querySelector(".player1-name").innerHTML = data["1"]
      document.querySelector(".player2-name").innerHTML = data["2"]
      document.querySelector(".player3-name").innerHTML = data["3"]
      document.querySelector(".player4-name").innerHTML = data["4"]
      if (data["game_state"] === "playing") {
        window.location.href = "/"
      }
    })
}

main()