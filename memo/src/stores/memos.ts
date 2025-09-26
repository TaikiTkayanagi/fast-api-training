import { defineStore } from "pinia"
import type { Memo, Memos } from "@/interface/Memo";

export const useMemosStore = defineStore('memos', {
    state: () => {
        return {
            response: {
                memos: [],
            } as Memos,
            isFeting: true,
            isFetingError: false,
        }
    },
    actions: {
        async fetchMemos() {
            try {
                const res = await fetch('http://localhost:8000/memos');
                this.response = await res.json() as Memos;
                console.log(JSON.stringify(this.response, null, 2)); // JSON風に展開
            } catch (error) {
                console.error('Error fetching memos:', error);
                this.isFetingError = true;
            } finally {
                this.isFeting = false;
            }
        },
        isEmpty() {
            return this.response.memos.length === 0
        }
    }
})