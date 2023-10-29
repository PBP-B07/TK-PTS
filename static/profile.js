
        async function openReadModal(id) {
            // You need to create an instance of the modal
            document.getElementById("readModalBody").innerHTML = ""
            let item = await getReview(id)
            const bookStarRating = generateStarRating(item[0].book__rating);
            const userStarRating = generateStarRating(item[0].star);
            let htmlString = `
                <h1>${item[0].book__title} ${bookStarRating}</h1>
                <p>You rated ${userStarRating} ${item[0].star} Star</p>
                <p style="font-style: italic; font-weight: 300px;>You commented "${item[0].description}"</p>
                <p class="text-secondary">${item[0].date_added}</p>
            `
            document.getElementById("readModalBody").innerHTML = htmlString
            const modal = new bootstrap.Modal(document.getElementById("readModal"));
            modal.show();
        }
        async function openEditModal(event, id) {
            event.stopPropagation();
            let item = await getReview(id)
            document.getElementById("star").value = item[0].star;
            document.getElementById("star-text").textContent = item[0].star + ' stars';
            document.getElementById("review_description").textContent = item[0].description;
            document.getElementById("review-editModalLabel").textContent = 'Edit Review for ' + item[0].book__title;
            document.getElementById("submit-review").onclick = function() {
                editReview(id);
            };
            const modal = new bootstrap.Modal(document.getElementById("editReviewModal"));
            modal.show();
        }
        async function openDeleteModal(event, id) {
            event.stopPropagation();
            document.getElementById("confirmDeleteBtn").onclick = function() {
                deleteReview(id)
            };
            const modal = new bootstrap.Modal(document.getElementById("deleteModal"));
            modal.show();
        }
        async function getReview(id){
            return fetch(`/profile/get_review/${id}/`).then((res) => res.json())
        }
        async function getReply(id){
            return fetch(`/profile/get_reply/${id}/`).then((res) => res.json())
        }
        document.getElementById("button_edit").onclick = editProfile

        async function editReview(id) {
            fetch(`/profile/edit_review/${id}/`, {
                method: "POST",
                body: new FormData(document.querySelector('#review-form'))
            }).then(refreshReviews)

            document.getElementById("review-form").reset()
            return false
        }
        async function deleteReview(id) {
            fetch(`/profile/delete_review/${id}/`, {
                method: 'POST',
            }).then(refreshReviews)
        }
        function stopPropagation(event){
            event.stopPropagation();
        }
        async function refreshReviews() {
            document.getElementById("reviews").innerHTML = ""
            let products = await getReviews()
            let htmlString = ``
            products.forEach((item) => {
                const userStarRating = generateStarRating(item.star);
                const bookStarRating = generateStarRating(item.book__rating);
                htmlString += `
                <div class="card card-special mb-2">
                    <div class="card-head"></div>
                    <div class="card-body" id="review-${item.pk}" onclick="openReadModal(${item.pk})">
                        <div class="d-flex justify-content-between">
                            <div class="col-8">
                                <h2 class="overflow-text" style="font-size: 28px;">${item.book__title}</h2>
                            </div><div class="col-4 d-flex justify-content-end">
                                <p style="font-size: 24px;">${bookStarRating} ${item.book__rating} Star</p>
                            </div>
                        </div>
                        <div class="d-flex justify-content-between align-items-center mb-0">
                            <p> You rated ${userStarRating} ${item.star} Star</p>
                            <p class="text-secondary">${item.date_added}</p>
                        </div>
                        <p class="overflow-text" style="font-style: italic; font-weight: 300px;">You commented "${item.description}"</p>
                        <a href="/books/${item.book__pk}" onclick="stopPropagation(event)" class="btn btn-primary">Lihat Buku</a>
                        <a onclick="openDeleteModal(event, ${item.pk})" class="btn btn-danger">Delete</a>
                        <button id="edit-review-${item.pk}" type="button" class="btn btn-primary" onclick="openEditModal(event, ${item.pk})">Edit</button>
                    </div>
                </div>
` 
            })

            document.getElementById("reviews").innerHTML = htmlString
        }
        async function refreshForums() {
            document.getElementById("forums").innerHTML = ""
            let products = await getForums()
            let htmlString = ``
            products.forEach((item) => {
                htmlString += `
                <div class="card mb-2">
                    <div class="card-body" id="forum-${item.pk}">
                        <div class="d-flex justify-content-between">
                            <div class="col-8">
                                <h2 style="font-size: 24px;">${item.subject}</h2>
                            </div><div class="col-4 d-flex justify-content-end">
                                <p class="text-secondary" style="font-size: 12px;">created by You</p>
                            </div>
                        </div>
                        <p style="font-weight: 300; font-style: italic;">${item.description}</p>
                        <p class="text-secondary">${item.date_added}</p>
                    </div>
                </div>` 
            })

            document.getElementById("forums").innerHTML = htmlString
        }
        function refreshStarText() {
            const slider = document.getElementById("star");
            document.getElementById("star-text").innerHTML = `${slider.value} stars`;
        }
        function generateStarRating(starCount) {
            starCount = Math.round(starCount)
            const filledStars = '<i class="fa fa-star"></i>'.repeat(starCount);
            const emptyStars = '<i class="fa fa-star-o"></i>'.repeat(5 - starCount);
            return filledStars + emptyStars;
        }

        refreshProfile()
        refreshReviews()
        refreshForums()
        refreshReplies()