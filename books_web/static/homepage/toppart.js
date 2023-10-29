const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultBox = document.getElementById('results-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData = (books) => {
    $.ajax({
        type: 'POST',
        url: 'search/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'books': books,
        },
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        },
        success: (res) => {
            var innerstring = "";
            for (var i = 0; i < res.length; i++) {

                innerstring = innerstring + "<a style='text-decoration: none;' href='/book/"
                    + res[i].id + "'><p style='color: black; text-decoration: none !important;'>" + res[i].title + "</p></a>";
                console.log(res[i])
            }
            resultBox.innerHTML = innerstring;
        },
        error: (err) => {
            console.log(err)
        },
    });
}

// searchInput.addEventListener('keyup', e => {
//     console.log(e.target.value)

//     if (resultBox.classList.contains('not-visible')) {
//         resultBox.classList.remove('not-visible')
//     }

//     sendSearchData(e.target.value)
// })

searchInput.addEventListener('input', function() {
    if (this.value.trim() === '') {
        resultBox.classList.add('not-visible'); 
    } else {
        resultBox.classList.remove('not-visible'); 
        sendSearchData(this.value); 
    }
});


