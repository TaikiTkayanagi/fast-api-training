import { defineStore } from "pinia";

export const useMemoForm = defineStore('memoForm', {
    state: () => {
        return {
            title: '',
            content: '',
            isPostSuccess: true,
            status: {
                deadLine: undefined as Date | undefined,
            }
        }
    },
    actions: {
        async post() {
            try {
                this.isPostSuccess = true;
                const body = JSON.stringify({
                    title: this.title,
                    content: this.content,
                    status: {
                        deadline: this.status.deadLine,
                        is_complete: false
                    }
                })
                console.log(body);
                const res = await fetch('http://localhost:8000/memos', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body
                });
            } catch (error) {
                console.error('Error posting memo:', error);
                this.isPostSuccess = false;
            }
        }
    }
});