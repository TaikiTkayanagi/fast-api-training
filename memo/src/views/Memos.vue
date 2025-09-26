<script setup lang="ts">
import { useMemosStore } from '@/stores/memos';

const memoStore = useMemosStore();
memoStore.fetchMemos();
</script>

<template>
    <div>
        <h1>Memos</h1>
        <template v-if="memoStore.isFeting">
            Loading...
        </template>
        <template v-else-if="memoStore.isFetingError">
            Error: 取得に失敗しました
        </template>
        <template v-else-if="memoStore.isEmpty()">
            メモがありません
        </template>
        <template v-else>
            <ul>
                <li v-for="memo in memoStore.response.memos" :key="memo.id">
                    <router-link :to="{name: 'memo-detail', params: {id: memo.id}}">{{ memo.title }}</router-link>
                </li>
            </ul>
        </template>
        <br/>
        <router-link :to="{name: 'memoForm'}">Create New Memo</router-link>
    </div>
</template>