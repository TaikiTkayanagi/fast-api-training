import { defineStore } from "pinia";

export const useMemoForm = defineStore('memoForm', {
    state: () => {
        return {
            title: '',
            content: '',
            isPostSuccess: true,
        }
    },
    actions: {
        async post() {
            try {
                this.isPostSuccess = true;
                const res = await fetch('http://localhost:8000/memos', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        title: this.title,
                        content: this.content,
                    })
                });
            } catch (error) {
                console.error('Error posting memo:', error);
                this.isPostSuccess = false;
            }
        }
    }
});