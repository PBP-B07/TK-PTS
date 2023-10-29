async function refreshForums() {
    document.getElementById("forum_container").innerHTML = ""
    const forums = await getForums()
    forums.reverse()
    let htmlString = ''
    let counter = 0
    const totalForums = forums.length
    for (const item of forums) {
        counter++
        htmlString += `
        <button class="row" id="forum_card" onclick="refreshReplies(${item.pk})" data-id="${item.id}">
                <div class="col s12 m6 l4">
                    <div class="card">  
                        <div class="card-content">
                            <h5 class="card-title", style="font-family: 'Poppins', sans-serif; font-weight: bold;">${item.subject} by ${item.user__username}</h5>
                            <p style="font-family: 'Poppins', sans-serif; font-weight: 400;">${item.description}</p>
                            <p style="font-family: 'Poppins', sans-serif; font-weight: 400;">Posted on: ${item.date_added}</p>
                        </div>
                    </div>
                </div>
            </button>

        `
    }
    document.getElementById("forum_container").innerHTML = htmlString
}

async function refreshReplies(forum_id) {
    document.getElementById("reply_box").innerHTML = ""
    const replies = await getReplies(forum_id)
    let htmlString = ''
    let counter = 0
    const totalReplies = replies.length
    for (const item of replies) {
        counter++
        htmlString += `
                <div class="reply-card">
                    <h5>By ${item.user__username}</h5>
                    <p class="reply">${item.message}</p>
                </div>
        `
    }
document.getElementById("reply_box").innerHTML = htmlString
document.getElementById("form_container").innerHTML = `
            <form id="message_form">
                <input type="textarea" class="input" id="message_input" placeholder="Enter your reply message"></input>
                <button type="submit" id="input_message" class="input_message")>Send</button>
            </form>
    `
// Add event listener to reply form
const messageForm = document.getElementById("message_form");
    messageForm.addEventListener("submit", function (event) {
        event.preventDefault();
        addReply(forum_id);
    });
}