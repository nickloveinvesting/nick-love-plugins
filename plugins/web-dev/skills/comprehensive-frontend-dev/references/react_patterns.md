# React Patterns & Best Practices

## Component Composition Patterns

### Compound Component Pattern
```typescript
interface TabsProps {
  defaultValue?: string;
  children: React.ReactNode;
}

interface TabsContextType {
  activeTab: string;
  setActiveTab: (tab: string) => void;
}

const TabsContext = createContext<TabsContextType | null>(null);

const Tabs: React.FC<TabsProps> & {
  List: React.FC<{ children: React.ReactNode }>;
  Tab: React.FC<{ value: string; children: React.ReactNode }>;
  Panel: React.FC<{ value: string; children: React.ReactNode }>;
} = ({ defaultValue = '', children }) => {
  const [activeTab, setActiveTab] = useState(defaultValue);

  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      <div className="tabs">{children}</div>
    </TabsContext.Provider>
  );
};

Tabs.List = ({ children }) => (
  <div role="tablist" className="tabs-list">{children}</div>
);

Tabs.Tab = ({ value, children }) => {
  const context = useContext(TabsContext);
  if (!context) throw new Error('Tab must be used within Tabs');

  return (
    <button
      role="tab"
      aria-selected={context.activeTab === value}
      onClick={() => context.setActiveTab(value)}
      className={cn('tab', { active: context.activeTab === value })}
    >
      {children}
    </button>
  );
};

Tabs.Panel = ({ value, children }) => {
  const context = useContext(TabsContext);
  if (!context) throw new Error('Panel must be used within Tabs');

  return context.activeTab === value ? (
    <div role="tabpanel" className="tab-panel">{children}</div>
  ) : null;
};
```

### Render Props Pattern
```typescript
interface DataFetcherProps<T> {
  url: string;
  children: (data: T | null, loading: boolean, error: Error | null) => React.ReactNode;
}

const DataFetcher = <T,>({ url, children }: DataFetcherProps<T>) => {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url);
        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err as Error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [url]);

  return <>{children(data, loading, error)}</>;
};

// Usage
<DataFetcher<User[]> url="/api/users">
  {(users, loading, error) => {
    if (loading) return <Spinner />;
    if (error) return <ErrorMessage error={error} />;
    return <UserList users={users} />;
  }}
</DataFetcher>
```

## Custom Hook Patterns

### State Management Hook
```typescript
interface UseToggleReturn {
  value: boolean;
  toggle: () => void;
  setTrue: () => void;
  setFalse: () => void;
}

const useToggle = (initialValue = false): UseToggleReturn => {
  const [value, setValue] = useState(initialValue);

  const toggle = useCallback(() => setValue(v => !v), []);
  const setTrue = useCallback(() => setValue(true), []);
  const setFalse = useCallback(() => setValue(false), []);

  return { value, toggle, setTrue, setFalse };
};
```

### API Integration Hook
```typescript
interface UseApiReturn<T> {
  data: T | null;
  loading: boolean;
  error: Error | null;
  refetch: () => Promise<void>;
}

const useApi = <T>(url: string, options?: RequestInit): UseApiReturn<T> => {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  const fetchData = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await fetch(url, options);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const result = await response.json();
      setData(result);
    } catch (err) {
      setError(err as Error);
    } finally {
      setLoading(false);
    }
  }, [url, options]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  return { data, loading, error, refetch: fetchData };
};
```

## Performance Optimization Patterns

### Memoization Strategies
```typescript
// Memoized expensive computation
const ExpensiveComponent: React.FC<{ data: ComplexData[] }> = ({ data }) => {
  const processedData = useMemo(() => {
    return data
      .filter(item => item.active)
      .sort((a, b) => a.priority - b.priority)
      .map(item => ({ ...item, computed: heavyComputation(item) }));
  }, [data]);

  return <DataVisualization data={processedData} />;
};

// Memoized callback functions
const TodoList: React.FC<{ todos: Todo[] }> = ({ todos }) => {
  const [filter, setFilter] = useState<'all' | 'active' | 'completed'>('all');

  const filteredTodos = useMemo(() => {
    return todos.filter(todo => {
      if (filter === 'all') return true;
      if (filter === 'active') return !todo.completed;
      return todo.completed;
    });
  }, [todos, filter]);

  const handleToggle = useCallback((id: string) => {
    // Toggle logic here
  }, []);

  return (
    <div>
      <FilterControls filter={filter} onFilterChange={setFilter} />
      {filteredTodos.map(todo => (
        <TodoItem key={todo.id} todo={todo} onToggle={handleToggle} />
      ))}
    </div>
  );
};
```

## Error Handling Patterns

### Error Boundary with Retry
```typescript
interface ErrorBoundaryState {
  hasError: boolean;
  error: Error | null;
  errorInfo: ErrorInfo | null;
}

class ErrorBoundary extends Component<
  { children: React.ReactNode; fallback?: React.ComponentType<{ error: Error; retry: () => void }> },
  ErrorBoundaryState
> {
  constructor(props: any) {
    super(props);
    this.state = { hasError: false, error: null, errorInfo: null };
  }

  static getDerivedStateFromError(error: Error): Partial<ErrorBoundaryState> {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    this.setState({ errorInfo });
    // Log error to monitoring service
    console.error('Error caught by boundary:', error, errorInfo);
  }

  retry = () => {
    this.setState({ hasError: false, error: null, errorInfo: null });
  };

  render() {
    if (this.state.hasError) {
      const FallbackComponent = this.props.fallback || DefaultErrorFallback;
      return <FallbackComponent error={this.state.error!} retry={this.retry} />;
    }

    return this.props.children;
  }
}

const DefaultErrorFallback: React.FC<{ error: Error; retry: () => void }> = ({ error, retry }) => (
  <div className="error-fallback">
    <h2>Something went wrong</h2>
    <details>{error.message}</details>
    <button onClick={retry}>Try again</button>
  </div>
);
```

## Testing Patterns

### Component Testing with React Testing Library
```typescript
// UserProfile.test.tsx
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { UserProfile } from './UserProfile';

const mockUser = {
  id: '1',
  name: 'John Doe',
  email: 'john@example.com',
  avatar: 'https://example.com/avatar.jpg'
};

describe('UserProfile', () => {
  it('displays user information correctly', () => {
    render(<UserProfile user={mockUser} />);
    
    expect(screen.getByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('john@example.com')).toBeInTheDocument();
    expect(screen.getByRole('img', { name: /john doe/i })).toHaveAttribute(
      'src', 
      mockUser.avatar
    );
  });

  it('handles edit mode correctly', async () => {
    const user = userEvent.setup();
    const mockOnSave = jest.fn();
    
    render(<UserProfile user={mockUser} onSave={mockOnSave} />);
    
    await user.click(screen.getByRole('button', { name: /edit/i }));
    
    const nameInput = screen.getByDisplayValue('John Doe');
    await user.clear(nameInput);
    await user.type(nameInput, 'Jane Doe');
    
    await user.click(screen.getByRole('button', { name: /save/i }));
    
    await waitFor(() => {
      expect(mockOnSave).toHaveBeenCalledWith({
        ...mockUser,
        name: 'Jane Doe'
      });
    });
  });
});
```

## Anti-Patterns to Avoid

### 1. Prop Drilling
❌ **Bad**
```typescript
// Passing props through multiple levels
const App = () => {
  const user = { name: 'John', theme: 'dark' };
  return <Layout user={user} />;
};

const Layout = ({ user }) => <Header user={user} />;
const Header = ({ user }) => <UserMenu user={user} />;
```

✅ **Good**
```typescript
// Use Context or state management
const UserContext = createContext();

const App = () => {
  const user = { name: 'John', theme: 'dark' };
  return (
    <UserContext.Provider value={user}>
      <Layout />
    </UserContext.Provider>
  );
};

const UserMenu = () => {
  const user = useContext(UserContext);
  return <div>Welcome, {user.name}</div>;
};
```

### 2. Mutating State Directly
❌ **Bad**
```typescript
const [todos, setTodos] = useState([]);

const addTodo = (text) => {
  todos.push({ id: Date.now(), text, completed: false });
  setTodos(todos); // Mutating state directly
};
```

✅ **Good**
```typescript
const [todos, setTodos] = useState([]);

const addTodo = (text) => {
  setTodos(prev => [...prev, { id: Date.now(), text, completed: false }]);
};
```

## Architecture Guidelines

### Component Organization
```
components/
├── ui/                 # Basic design system components
│   ├── Button/
│   ├── Input/
│   └── Modal/
├── forms/             # Form-specific components  
│   ├── ContactForm/
│   └── LoginForm/
├── layout/            # Layout components
│   ├── Header/
│   ├── Sidebar/
│   └── Footer/
└── features/          # Feature-specific components
    ├── UserProfile/
    ├── ProductCatalog/
    └── ShoppingCart/
```

### State Management Architecture
```typescript
// Global state structure
interface AppState {
  user: {
    profile: UserProfile | null;
    preferences: UserPreferences;
    isAuthenticated: boolean;
  };
  ui: {
    theme: 'light' | 'dark';
    sidebar: { isOpen: boolean };
    notifications: Notification[];
  };
  data: {
    products: Product[];
    cart: CartItem[];
    orders: Order[];
  };
}

// Separate stores for different domains
const useUserStore = create((set) => ({...}));
const useUIStore = create((set) => ({...}));
const useDataStore = create((set) => ({...}));
```

This guide provides practical patterns proven in production environments. Apply these patterns based on your specific use case and requirements.
