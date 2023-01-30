  function updateSelected() {
            selected = [];
            var checkboxes = document.querySelectorAll("#checkboxes input[type='checkbox']");
            for (var i = 0; i < checkboxes.length; i++) {
                if (checkboxes[i].checked) {
                  selected = [];
                    selected.push(checkboxes[i].value);
                    break;
                }
            }
            for (var i = 0; i < checkboxes.length; i++) {
    checkboxes[i].checked = false;
        }document.querySelector("input[value='" + selected[0] + "'").checked = true;
      }
        function displaySelected() {
    document.getElementById("selected").innerHTML = "" + selected.join(', ');
    document.getElementById("selected").classList.add("selected-text");
    var audio = document.getElementById("myAudio");
    setTimeout(function() {
        audio.src = audioFiles[selected[0]];
        audio.play();
    }, 2000);
}
