class TemplateLibrary:
    """
    Section 3.2: Proven Component Library
    Contains C code templates for systems programming patterns.
    """

    LOCK_FREE_QUEUE = """
/* Lock-free Queue Implementation */
typedef struct node {
    void *data;
    struct node *next;
} node_t;

typedef struct queue {
    node_t *head;
    node_t *tail;
} queue_t;

void enqueue(queue_t *q, void *data) {
    node_t *node = malloc(sizeof(node_t));
    node->data = data;
    node->next = NULL;
    node_t *last, *next;
    while (1) {
        last = q->tail;
        next = last->next;
        if (last == q->tail) {
            if (next == NULL) {
                if (__sync_bool_compare_and_swap(&last->next, next, node)) break;
            } else {
                __sync_bool_compare_and_swap(&q->tail, last, next);
            }
        }
    }
    __sync_bool_compare_and_swap(&q->tail, last, node);
}
"""

    ARENA_ALLOCATOR = """
/* Arena Allocator Implementation */
#include <stdlib.h>
#include <stddef.h>

typedef struct Arena {
    char *buffer;
    size_t size;
    size_t offset;
} Arena;

Arena* arena_init(size_t size) {
    Arena *arena = malloc(sizeof(Arena));
    arena->buffer = malloc(size);
    arena->size = size;
    arena->offset = 0;
    return arena;
}

void* arena_alloc(Arena *arena, size_t size) {
    if (arena->offset + size > arena->size) return NULL;
    void *ptr = &arena->buffer[arena->offset];
    arena->offset += size;
    return ptr;
}

void arena_reset(Arena *arena) {
    arena->offset = 0;
}

void arena_destroy(Arena *arena) {
    free(arena->buffer);
    free(arena);
}
"""

    OBJECT_POOL = """
/* Object Pool Implementation */
#include <stdlib.h>
#include <stdbool.h>

typedef struct ObjectPool {
    void **pool;
    bool *used;
    size_t object_size;
    size_t pool_size;
} ObjectPool;

ObjectPool* pool_init(size_t object_size, size_t pool_size) {
    ObjectPool *op = malloc(sizeof(ObjectPool));
    op->pool = malloc(pool_size * sizeof(void*));
    op->used = calloc(pool_size, sizeof(bool));
    op->object_size = object_size;
    op->pool_size = pool_size;
    for(size_t i = 0; i < pool_size; i++) {
        op->pool[i] = malloc(object_size);
    }
    return op;
}

void* pool_alloc(ObjectPool *op) {
    for(size_t i = 0; i < op->pool_size; i++) {
        if(!op->used[i]) {
            op->used[i] = true;
            return op->pool[i];
        }
    }
    return NULL;
}

void pool_free(ObjectPool *op, void *ptr) {
    for(size_t i = 0; i < op->pool_size; i++) {
        if(op->pool[i] == ptr) {
            op->used[i] = false;
            return;
        }
    }
}

void pool_destroy(ObjectPool *op) {
    for(size_t i = 0; i < op->pool_size; i++) {
        free(op->pool[i]);
    }
    free(op->pool);
    free(op->used);
    free(op);
}
"""

    REFERENCE_COUNTING = """
/* Simple Reference Counting Pattern */
#include <stdlib.h>

typedef struct RefCounted {
    int count;
    void (*destroy)(struct RefCounted *);
} RefCounted;

void ref_retain(RefCounted *obj) {
    if (obj) obj->count++;
}

void ref_release(RefCounted *obj) {
    if (obj) {
        obj->count--;
        if (obj->count <= 0) {
            if (obj->destroy) obj->destroy(obj);
            free(obj);
        }
    }
}

RefCounted* ref_init(size_t size, void (*destroy)(RefCounted *)) {
    RefCounted *obj = malloc(size);
    obj->count = 1;
    obj->destroy = destroy;
    return obj;
}
"""

    CONSERVATIVE_GC = """
/* Conservative Garbage Collector Stub (Boehm GC integration pattern) */
#include <gc.h>
#include <stdlib.h>

void* gc_alloc(size_t size) {
    return GC_MALLOC(size);
}

void gc_init() {
    GC_INIT();
}
"""

    INTRUSIVE_LIST = """
/* Intrusive Linked List Implementation */
#include <stddef.h>

typedef struct list_head {
    struct list_head *next, *prev;
} list_head;

#define container_of(ptr, type, member) ({                      \\
        const typeof( ((type *)0)->member ) *__mptr = (ptr);    \\
        (type *)( (char *)__mptr - offsetof(type,member) );})

#define list_entry(ptr, type, member) \\
    container_of(ptr, type, member)

static inline void list_add(struct list_head *new, struct list_head *head) {
    new->next = head->next;
    new->prev = head;
    head->next->prev = new;
    head->next = new;
}
"""

    WORK_STEALING_SCHEDULER = """
/* Work-stealing Scheduler Pattern (Section 6.1) */
#include <pthread.h>
#include <stdbool.h>

typedef struct ws_deque {
    void **buffer;
    size_t size;
    volatile long top, bottom;
} ws_deque_t;

void ws_push(ws_deque_t *q, void *data) {
    long b = q->bottom;
    q->buffer[b % q->size] = data;
    q->bottom = b + 1;
}

void* ws_pop(ws_deque_t *q) {
    long b = q->bottom - 1;
    q->bottom = b;
    long t = q->top;
    if (t <= b) {
        void *data = q->buffer[b % q->size];
        if (t == b) {
            if (!__sync_bool_compare_and_swap(&q->top, t, t + 1)) data = NULL;
            q->bottom = t + 1;
        }
        return data;
    }
    q->bottom = t;
    return NULL;
}

void* ws_steal(ws_deque_t *q) {
    long t = q->top;
    long b = q->bottom;
    if (t < b) {
        void *data = q->buffer[t % q->size];
        if (!__sync_bool_compare_and_swap(&q->top, t, t + 1)) return NULL;
        return data;
    }
    return NULL;
}
"""

    COPY_ON_WRITE = """
/* Copy-on-Write (COW) Memory Pattern (Section 5.2) */
#include <sys/mman.h>
#include <unistd.h>
#include <string.h>

void* cow_init(size_t size) {
    return mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
}

void* cow_fork_child(void *parent_ptr, size_t size) {
    /* In a real OS fork() handles COW, this is a simulated pattern */
    void *child_ptr = mmap(NULL, size, PROT_READ, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    /* In COW, child points to same physical pages as parent until write */
    return parent_ptr;
}
"""

    TCP_SERVER = """
/* TCP Server Pattern (Section 6.2) */
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

int start_tcp_server(int port) {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in address;
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(port);
    bind(server_fd, (struct sockaddr *)&address, sizeof(address));
    listen(server_fd, 3);
    return server_fd;
}
"""

    SHARED_MEMORY = """
/* POSIX Shared Memory Pattern (Section 6.2) */
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

void* create_shared_memory(const char *name, size_t size) {
    int shm_fd = shm_open(name, O_CREAT | O_RDWR, 0666);
    ftruncate(shm_fd, size);
    return mmap(0, size, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
}
"""

    RAII_CLEANUP = """
/* RAII-style Cleanup Pattern (Section 7.2) */
#define RAII_VARIABLE(type, name, setup, cleanup) \\
    type name __attribute__((cleanup(cleanup))) = setup

void close_file(int *fd) {
    if (*fd >= 0) {
        printf("RAII: Closing file descriptor %d\\n", *fd);
        close(*fd);
    }
}
"""

    THREAD_POOL = """
/* POSIX Thread Pool Template */
#include <pthread.h>
#include <stdlib.h>

typedef struct {
    void (*function)(void *);
    void *argument;
} threadpool_task_t;

typedef struct {
    pthread_mutex_t lock;
    pthread_cond_t notify;
    pthread_t *threads;
    threadpool_task_t *queue;
    int thread_count;
    int queue_size;
    int head;
    int tail;
    int count;
    int shutdown;
} threadpool_t;

/* ... (Omitted full implementation for brevity in template) ... */
"""

    SIGNAL_HANDLER = """
/* Async-safe Signal Handler */
#include <signal.h>
#include <unistd.h>

volatile sig_atomic_t keep_running = 1;

void handle_signal(int sig) {
    keep_running = 0;
    const char *msg = "Caught signal, shutting down...\\n";
    write(STDOUT_FILENO, msg, 32);
}

void setup_signals() {
    struct sigaction sa;
    sa.sa_handler = handle_signal;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;
    sigaction(SIGINT, &sa, NULL);
    sigaction(SIGTERM, &sa, NULL);
}
"""

    @classmethod
    def get_template(cls, name):
        return getattr(cls, name.upper(), None)
