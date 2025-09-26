import { defineStore } from "pinia"
import type { Memo } from "@/interface/Memo";

export const useMemoStore = defineStore('memo', {
    state: () => {
        return {
            memo: {} as Memo,
            isFeting: true,
            isFetingError: false,
        }
    },
    actions: {
        async fetchMemos(id: number) {
            try {
                const res = await fetch('http://localhost:8000/memos/' + id);
                const json = await res.json() as {memo: Memo} | null;
                if (json?.memo) {
                    this.memo = json.memo;
                }
            } catch (error) {
                console.error('Error fetching memos:', error);
                this.isFetingError = true;
            } finally {
                this.isFeting = false;
            }
        },
    }
})