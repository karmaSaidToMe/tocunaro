let ethereumButton = document.querySelector('#enableEth');
let title = document.querySelector('#title');

ethereumButton.addEventListener('click', () => {
    getAccount();
});

async function getAccount() {
    let accounts = await ethereum.request({ method: 'eth_requestAccounts' });
    let account = accounts[0];
    $("#title, #enableEth").fadeOut(1000, () => {
        title.innerHTML = account;
    });
    $("#title").fadeIn(700, () => {});
}
