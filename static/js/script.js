document.addEventListener("DOMContentLoaded", function () {
    // ---------- Choice Management ------------
    const choicesContainer = document.getElementById("choices-container");
    const addOptionBtn = document.getElementById("add-option-btn");
    const messageElement = document.getElementById("option-limit-message");

    function getCurrentVisibleOptionCount() {
        return choicesContainer.querySelectorAll('.choice-option:not([style*="display: none"])').length;
    }

    function addChoice() {
        const currentVisibleOptions = getCurrentVisibleOptionCount();

        if (currentVisibleOptions < 6) {
            console.log("Adding new option with placeholder:", `Option ${currentVisibleOptions + 1}`);
            const newChoice = document.createElement('div');
            newChoice.className = 'choice-option';
            newChoice.innerHTML = `
                <div class="input-container">
                    <input type="text" class="choice-input" placeholder="Option ${currentVisibleOptions + 1}" name="choice_text_${currentVisibleOptions + 1}">
                    <span class="delete-option">✕</span>
                </div>
            `;

            choicesContainer.insertBefore(newChoice, addOptionBtn);

            updatePlaceholders();

            if (getCurrentVisibleOptionCount() >= 6) {
                addOptionBtn.disabled = true;
                messageElement.style.display = "block";
            }
        } else {
            console.log("Cannot add more options. Maximum limit reached.");
        }
    }

    function removeChoice(element) {
        const choiceOption = element.closest('.choice-option');
        choiceOption.style.display = 'none';
        choiceOption.querySelector('input[type="text"]').disabled = true;

        console.log("Marked an option as deleted. Updating placeholders...");

        updatePlaceholders();

        if (getCurrentVisibleOptionCount() < 6) {
            addOptionBtn.disabled = false;
            messageElement.style.display = "none";
        }
    }

    function updatePlaceholders() {
        const choiceInputs = choicesContainer.querySelectorAll('.choice-option input[type="text"]:not([disabled])');
        console.log("Updating placeholders for current options:", choiceInputs.length);

        choiceInputs.forEach((input, index) => {
            input.placeholder = `Option ${index + 1}`;
            console.log(`Set placeholder for option ${index + 1}:`, input.placeholder);
        });
    }

    if (addOptionBtn) {
        addOptionBtn.addEventListener("click", addChoice);
    }

    if (choicesContainer) {
        choicesContainer.addEventListener("click", function (event) {
            if (event.target.classList.contains("delete-option")) {
                console.log("Delete button clicked");
                removeChoice(event.target);
            }
        });
    }

    function closeShareModal() {
        const shareModal = document.getElementById("shareModal");
        if (shareModal) {
            shareModal.style.display = "none";
        }
    }

    const closeModalButton = document.querySelector(".close-btn");
    if (closeModalButton) {
        closeModalButton.addEventListener("click", closeShareModal);
    }

    // ---------- Responsive Navigation Menu ------------
    const menuToggle = document.getElementById("menu-toggle");
    const navList = document.getElementById("nav-list");

    menuToggle.addEventListener("click", function () {
        navList.classList.toggle("show");
    });

    // ---------- Search Function ------------
    const searchInput = document.getElementById("search-input");
    const clearBtn = document.getElementById("clear-btn");

    if (searchInput && clearBtn) {
        searchInput.addEventListener("input", function () {
            if (searchInput.value.trim() !== "") {
                clearBtn.style.display = "block"; 
            } else {
                clearBtn.style.display = "none"; 
            }
        });

    }

    clearBtn.addEventListener("click", function () {
        searchInput.value = "";
        clearBtn.style.display = "none";
        searchInput.focus(); 
    });
});

// ---------- Copy to Clipboard Function ------------
function copyToClipboard() {
    const shareLink = document.getElementById("shareLink");
    if (shareLink) {
        navigator.clipboard.writeText(shareLink.value)
            .then(() => alert("Link copied to clipboard!"))
            .catch(err => console.error("Failed to copy link:", err));
    }
}

