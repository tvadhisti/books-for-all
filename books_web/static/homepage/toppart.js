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
        success: (res)=> {
            console.log(res)
        },
        error: (err)=> {
            console.log(err)
        },
    });
}

searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value)

    if(resultBox.classList.contains('not-visible')){
        resultBox.classList.remove('not-visible')
    }

    sendSearchData(e.target.value)
})


