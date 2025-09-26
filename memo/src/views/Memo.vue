<script setup lang="ts">
import { useMemoStore } from '@/stores/memo';

const props = defineProps<{
    id: number
}>()

const memoStore = useMemoStore()
memoStore.fetchMemos(props.id)
</script>

<template>
    <div>
        <h1>Memo</h1>
        <template v-if="memoStore.isFeting">
            <p>Loading...</p>
        </template>
        <template v-else-if="memoStore.isFetingError">
            <p>取得に失しましたｔ</p>
        </template>
        <template v-else>
            <h2>{{ memoStore.memo.id }}: {{ memoStore.memo.title }}</h2>
            <p>{{ memoStore.memo.content }}</p>
        </template>
    </div>
</template>