import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Tuple, Union

from redis_sdk.typing import FloatMinMaxT, ValueT
from redis_sdk.utils import GeoSearchResult

class Commands:
    def bitcount(
        self, key: str, start: Optional[int] = None, end: Optional[int] = None
    ) -> int: ...
    def bitfield(self, key: str) -> "BitFieldCommands": ...
    def bitfield_ro(self, key: str) -> "BitFieldROCommands": ...
    def bitop(
        self, operation: Literal["AND", "OR", "XOR", "NOT"], destkey: str, *keys: str
    ) -> int: ...
    def bitpos(
        self,
        key: str,
        bit: Literal[0, 1],
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> int: ...
    def getbit(self, key: str, offset: int) -> Literal[0, 1]: ...
    def setbit(self, key: str, offset: int, value: Literal[0, 1]) -> int: ...
    def ping(self, message: Optional[str] = None) -> str: ...
    def echo(self, message: str) -> str: ...
    def copy(self, source: str, destination: str, replace: bool = False) -> bool: ...
    def delete(self, *keys: str) -> int: ...
    def exists(self, *keys: str) -> int: ...
    def expire(
        self,
        key: str,
        seconds: Union[int, datetime.timedelta],
        nx: bool = False,
        xx: bool = False,
        gt: bool = False,
        lt: bool = False,
    ) -> bool: ...
    def expireat(
        self,
        key: str,
        unix_time_seconds: Union[int, datetime.datetime],
        nx: bool = False,
        xx: bool = False,
        gt: bool = False,
        lt: bool = False,
    ) -> bool: ...
    def keys(self, pattern: str) -> List[str]: ...
    def persist(self, key: str) -> bool: ...
    def pexpire(
        self,
        key: str,
        milliseconds: Union[int, datetime.timedelta],
        nx: bool = False,
        xx: bool = False,
        gt: bool = False,
        lt: bool = False,
    ) -> bool: ...
    def pexpireat(
        self,
        key: str,
        unix_time_milliseconds: Union[int, datetime.datetime],
        nx: bool = False,
        xx: bool = False,
        gt: bool = False,
        lt: bool = False,
    ) -> bool: ...
    def pttl(self, key: str) -> int: ...
    def randomkey(self) -> Optional[str]: ...
    def rename(self, key: str, newkey: str) -> bool: ...
    def renamenx(self, key: str, newkey: str) -> bool: ...
    def scan(
        self,
        cursor: int,
        match: Optional[str] = None,
        count: Optional[int] = None,
        type: Optional[str] = None,
    ) -> Tuple[int, List[str]]: ...
    def touch(self, *keys: str) -> int: ...
    def ttl(self, key: str) -> int: ...
    def type(self, key: str) -> Optional[str]: ...
    def unlink(self, *keys: str) -> int: ...
    def geoadd(
        self,
        key: str,
        *members: Tuple[float, float, str],
        nx: bool = False,
        xx: bool = False,
        ch: bool = False,
    ) -> int: ...
    def geodist(
        self,
        key: str,
        member1: str,
        member2: str,
        unit: Literal["M", "KM", "FT", "MI"] = "M",
    ) -> Optional[float]: ...
    def geohash(self, key: str, *members: str) -> List[Optional[str]]: ...
    def geopos(
        self, key: str, *members: str
    ) -> List[Union[Tuple[float, float], None]]: ...
    def georadius(
        self,
        key: str,
        longitude: float,
        latitude: float,
        radius: float,
        unit: Literal["M", "KM", "FT", "MI"],
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
        count: Optional[int] = None,
        any: bool = False,
        order: Optional[Literal["ASC", "DESC"]] = None,
        store: Optional[str] = None,
        storedist: Optional[str] = None,
    ) -> Union[List[Union[str, GeoSearchResult]], int]: ...
    def georadius_ro(
        self,
        key: str,
        longitude: float,
        latitude: float,
        radius: float,
        unit: Literal["M", "KM", "FT", "MI"],
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
        count: Optional[int] = None,
        any: bool = False,
        order: Optional[Literal["ASC", "DESC"]] = None,
    ) -> List[Union[str, GeoSearchResult]]: ...
    def georadiusbymember(
        self,
        key: str,
        member: str,
        radius: float,
        unit: Literal["M", "KM", "FT", "MI"],
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
        count: Optional[int] = None,
        any: bool = False,
        order: Optional[Literal["ASC", "DESC"]] = None,
        store: Optional[str] = None,
        storedist: Optional[str] = None,
    ) -> Union[List[Union[str, GeoSearchResult]], int]: ...
    def georadiusbymember_ro(
        self,
        key: str,
        member: str,
        radius: float,
        unit: Literal["M", "KM", "FT", "MI"],
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
        count: Optional[int] = None,
        any: bool = False,
        order: Optional[Literal["ASC", "DESC"]] = None,
    ) -> List[Union[str, GeoSearchResult]]: ...
    def geosearch(
        self,
        key: str,
        unit: Literal["M", "KM", "FT", "MI"],
        member: Optional[str] = None,
        longitude: Optional[float] = None,
        latitude: Optional[float] = None,
        radius: Optional[float] = None,
        width: Optional[float] = None,
        height: Optional[float] = None,
        order: Optional[Literal["ASC", "DESC"]] = None,
        count: Optional[int] = None,
        any: bool = False,
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
    ) -> List[Union[str, GeoSearchResult]]: ...
    def geosearchstore(
        self,
        destination: str,
        source: str,
        member: Optional[str] = None,
        longitude: Optional[float] = None,
        latitude: Optional[float] = None,
        unit: Literal["M", "KM", "FT", "MI"] = "M",
        radius: Optional[float] = None,
        width: Optional[float] = None,
        height: Optional[float] = None,
        order: Optional[Literal["ASC", "DESC"]] = None,
        count: Optional[int] = None,
        any: bool = False,
        storedist: bool = False,
    ) -> int: ...
    def hdel(self, key: str, *fields: str) -> int: ...
    def hexists(self, key: str, field: str) -> bool: ...
    def hget(self, key: str, field: str) -> Optional[str]: ...
    def hgetall(self, key: str) -> Dict[str, str]: ...
    def hincrby(self, key: str, field: str, increment: int) -> int: ...
    def hincrbyfloat(self, key: str, field: str, increment: float) -> float: ...
    def hkeys(self, key: str) -> List[str]: ...
    def hlen(self, key: str) -> int: ...
    def hmget(self, key: str, *fields: str) -> List[Optional[str]]: ...
    def hmset(self, key: str, values: Mapping[str, ValueT]) -> bool: ...
    def hrandfield(
        self, key: str, count: Optional[int] = None, withvalues: bool = False
    ) -> Union[str, None, List[str], Dict[str, str]]: ...
    def hscan(
        self,
        key: str,
        cursor: int,
        match: Optional[str] = None,
        count: Optional[int] = None,
    ) -> Tuple[int, Dict[str, str]]: ...
    def hset(
        self,
        key: str,
        field: Optional[str] = None,
        value: Optional[str] = None,
        values: Optional[Mapping[str, ValueT]] = None,
    ) -> int: ...
    def hsetnx(self, key: str, field: str, value: ValueT) -> bool: ...
    def hstrlen(self, key: str, field: str) -> int: ...
    def hvals(self, key: str) -> List[str]: ...
    def pfadd(self, key: str, *elements: ValueT) -> bool: ...
    def pfcount(self, *keys: str) -> int: ...
    def pfmerge(self, destkey: str, *sourcekeys: str) -> bool: ...
    def lindex(self, key: str, index: int) -> Optional[str]: ...
    def linsert(
        self,
        key: str,
        where: Literal["BEFORE", "AFTER"],
        pivot: ValueT,
        element: str,
    ) -> int: ...
    def llen(self, key: str) -> int: ...
    def lmove(
        self,
        source: str,
        destination: str,
        wherefrom: Literal["LEFT", "RIGHT"] = "LEFT",
        whereto: Literal["LEFT", "RIGHT"] = "RIGHT",
    ) -> Optional[str]: ...
    def lpop(
        self, key: str, count: Optional[int] = None
    ) -> Union[str, List[str], None]: ...
    def lpos(
        self,
        key: str,
        element: ValueT,
        rank: Optional[int] = None,
        count: Optional[int] = None,
        maxlen: Optional[int] = None,
    ) -> Union[(Optional[int]), List[int]]: ...
    def lpush(self, key: str, *elements: ValueT) -> int: ...
    def lpushx(self, key: str, *elements: ValueT) -> int: ...
    def lrange(self, key: str, start: int, stop: int) -> List[str]: ...
    def lrem(self, key: str, count: int, element: ValueT) -> int: ...
    def lset(self, key: str, index: int, element: ValueT) -> bool: ...
    def ltrim(self, key: str, start: int, stop: int) -> str: ...
    def rpop(
        self, key: str, count: Optional[int] = None
    ) -> Union[str, List[str], None]: ...
    def rpoplpush(self, source: str, destination: str) -> Optional[str]: ...
    def rpush(self, key: str, *elements: ValueT) -> int: ...
    def rpushx(self, key: str, *elements: ValueT) -> int: ...
    def publish(self, channel: str, message: ValueT) -> int: ...
    def eval(
        self,
        script: str,
        keys: Optional[List[str]] = None,
        args: Optional[List[str]] = None,
    ) -> Any: ...
    def evalsha(
        self,
        sha1: str,
        keys: Optional[List[str]] = None,
        args: Optional[List[str]] = None,
    ) -> Any: ...
    def dbsize(self) -> int: ...
    def flushall(
        self, flush_type: Optional[Literal["ASYNC", "SYNC"]] = None
    ) -> bool: ...
    def flushdb(
        self, flush_type: Optional[Literal["ASYNC", "SYNC"]] = None
    ) -> bool: ...
    def time(self) -> Tuple[int, int]: ...
    def sadd(self, key: str, *members: ValueT) -> int: ...
    def scard(self, key: str) -> int: ...
    def sdiff(self, *keys: str) -> List[str]: ...
    def sdiffstore(self, destination: str, *keys: str) -> int: ...
    def sinter(self, *keys: str) -> List[str]: ...
    def sinterstore(self, destination: str, *keys: str) -> int: ...
    def sismember(self, key: str, member: ValueT) -> bool: ...
    def smismember(self, key: str, *members: ValueT) -> List[bool]: ...
    def smembers(self, key: str) -> List[str]: ...
    def smove(self, source: str, destination: str, member: ValueT) -> bool: ...
    def spop(
        self, key: str, count: Optional[int] = None
    ) -> Union[str, List[str], None]: ...
    def srandmember(
        self, key: str, count: Optional[int] = None
    ) -> Union[str, List[str], None]: ...
    def srem(self, key: str, *members: ValueT) -> int: ...
    def sscan(
        self,
        key: str,
        cursor: int = 0,
        match: Optional[str] = None,
        count: Optional[int] = None,
    ) -> Tuple[int, List[str]]: ...
    def sunion(self, *keys: str) -> List[str]: ...
    def sunionstore(self, destination: str, *keys: str) -> int: ...
    def zadd(
        self,
        key: str,
        scores: Dict[str, float],
        nx: bool = False,
        xx: bool = False,
        gt: bool = False,
        lt: bool = False,
        ch: bool = False,
        incr: bool = False,
    ) -> Union[int, float, None]: ...
    def zcard(self, key: str) -> int: ...
    def zcount(self, key: str, min: FloatMinMaxT, max: FloatMinMaxT) -> int: ...
    def zdiff(
        self, keys: List[str], withscores: bool = False
    ) -> Union[List[str], List[Tuple[str, float]]]: ...
    def zdiffstore(self, destination: str, keys: List[str]) -> int: ...
    def zincrby(self, key: str, increment: float, member: str) -> float: ...
    def zinter(
        self,
        keys: List[str],
        weights: Union[List[float], List[int], None] = None,
        aggregate: Optional[Literal["SUM", "MIN", "MAX"]] = None,
        withscores: bool = False,
    ) -> Union[List[str], List[Tuple[str, float]]]: ...
    def zinterstore(
        self,
        destination: str,
        keys: List[str],
        weights: Union[List[float], List[int], None] = None,
        aggregate: Optional[Literal["SUM", "MIN", "MAX"]] = None,
    ) -> int: ...
    def zlexcount(self, key: str, min: str, max: str) -> int: ...
    def zmscore(self, key: str, members: List[str]) -> List[Optional[float]]: ...
    def zpopmax(
        self, key: str, count: Optional[int] = None
    ) -> List[Tuple[str, float]]: ...
    def zpopmin(
        self, key: str, count: Optional[int] = None
    ) -> List[Tuple[str, float]]: ...
    def zrandmember(
        self, key: str, count: Optional[int] = None, withscores: bool = False
    ) -> Union[str, None, List[str], List[Tuple[str, float]]]: ...
    def zrange(
        self,
        key: str,
        start: FloatMinMaxT,
        stop: FloatMinMaxT,
        sortby: Optional[Literal["BYSCORE", "BYLEX"]] = None,
        rev: bool = False,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        withscores: bool = False,
    ) -> Union[List[str], List[Tuple[str, float]]]: ...
    def zrangebylex(
        self,
        key: str,
        min: str,
        max: str,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> List[str]: ...
    def zrangebyscore(
        self,
        key: str,
        min: FloatMinMaxT,
        max: FloatMinMaxT,
        withscores: bool = False,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> Union[List[str], List[Tuple[str, float]]]: ...
    def zrangestore(
        self,
        dst: str,
        src: str,
        min: FloatMinMaxT,
        max: FloatMinMaxT,
        sortby: Optional[Literal["BYSCORE", "BYLEX"]] = None,
        rev: bool = False,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> int: ...
    def zrank(self, key: str, member: str) -> Optional[int]: ...
    def zrem(self, key: str, *members: str) -> int: ...
    def zremrangebylex(self, key: str, min: str, max: str) -> int: ...
    def zremrangebyrank(self, key: str, start: int, stop: int) -> int: ...
    def zremrangebyscore(
        self, key: str, min: FloatMinMaxT, max: FloatMinMaxT
    ) -> int: ...
    def zrevrange(
        self, key: str, start: int, stop: int, withscores: bool = False
    ) -> Union[List[str], List[Tuple[str, float]]]: ...
    def zrevrangebylex(
        self,
        key: str,
        max: str,
        min: str,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> List[str]: ...
    def zrevrangebyscore(
        self,
        key: str,
        max: FloatMinMaxT,
        min: FloatMinMaxT,
        withscores: bool = False,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> Union[List[str], List[Tuple[str, float]]]: ...
    def zrevrank(self, key: str, member: str) -> Optional[int]: ...
    def zscan(
        self,
        key: str,
        cursor: int,
        match: Optional[str] = None,
        count: Optional[int] = None,
    ) -> Tuple[int, List[Tuple[str, float]]]: ...
    def zscore(self, key: str, member: str) -> Optional[float]: ...
    def zunion(
        self,
        keys: List[str],
        weights: Optional[List[float]] = None,
        aggregate: Optional[Literal["SUM", "MIN", "MAX"]] = None,
        withscores: bool = False,
    ) -> Union[List[str], List[Tuple[str, float]]]: ...
    def zunionstore(
        self,
        destination: str,
        keys: List[str],
        weights: Optional[List[float]] = None,
        aggregate: Optional[Literal["SUM", "MIN", "MAX"]] = None,
    ) -> int: ...
    def append(self, key: str, value: str) -> int: ...
    def decr(self, key: str) -> int: ...
    def decrby(self, key: str, decrement: int) -> int: ...
    def get(self, key: str) -> Optional[str]: ...
    def getdel(self, key: str) -> Optional[str]: ...
    def getex(
        self,
        key: str,
        ex: Optional[int] = None,
        px: Optional[int] = None,
        exat: Optional[int] = None,
        pxat: Optional[int] = None,
        persist: Optional[bool] = None,
    ) -> Optional[str]: ...
    def getrange(self, key: str, start: int, end: int) -> str: ...
    def getset(self, key: str, value: ValueT) -> Optional[str]: ...
    def incr(self, key: str) -> int: ...
    def incrby(self, key: str, increment: int) -> int: ...
    def incrbyfloat(self, key: str, increment: float) -> float: ...
    def mget(self, *keys: str) -> List[Optional[str]]: ...
    def mset(self, values: Mapping[str, ValueT]) -> Literal[True]: ...
    def msetnx(self, values: Mapping[str, ValueT]) -> bool: ...
    def psetex(self, key: str, milliseconds: int, value: str) -> Literal[True]: ...
    def set(
        self,
        key: str,
        value: ValueT,
        nx: bool = False,
        xx: bool = False,
        get: bool = False,
        ex: Optional[int] = None,
        px: Optional[int] = None,
        exat: Optional[int] = None,
        pxat: Optional[int] = None,
        keepttl: bool = False,
    ) -> Optional[str]: ...
    def setex(self, key: str, seconds: int, value: ValueT) -> Literal[True]: ...
    def setnx(self, key: str, value: ValueT) -> bool: ...
    def setrange(self, key: str, offset: int, value: str) -> int: ...
    def strlen(self, key: str) -> int: ...
    def substr(self, key: str, start: int, end: int) -> str: ...
    def script_exists(self, *sha1: str) -> List[bool]: ...
    def script_flush(
        self, flush_type: Optional[Literal["ASYNC", "SYNC"]] = None
    ) -> bool: ...
    def script_load(self, script: str) -> str: ...

class AsyncCommands:
    def __init__(self): ...
    async def bitcount(
        self, key: str, start: Optional[int] = None, end: Optional[int] = None
    ) -> int: ...
    def bitfield(self, key: str) -> "AsyncBitFieldCommands": ...
    def bitfield_ro(self, key: str) -> "AsyncBitFieldROCommands": ...
    async def bitop(
        self, operation: Literal["AND", "OR", "XOR", "NOT"], destkey: str, *keys: str
    ) -> int: ...
    async def bitpos(
        self,
        key: str,
        bit: Literal[0, 1],
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> int: ...
    async def getbit(self, key: str, offset: int) -> Literal[0, 1]: ...
    async def setbit(self, key: str, offset: int, value: Literal[0, 1]) -> int: ...
    async def ping(self, message: Optional[str] = None) -> str: ...
    async def echo(self, message: str) -> str: ...
    async def copy(
        self, source: str, destination: str, replace: bool = False
    ) -> bool: ...
    async def delete(self, *keys: str) -> int: ...
    async def exists(self, *keys: str) -> int: ...
    async def expire(
        self,
        key: str,
        seconds: Union[int, datetime.timedelta],
        nx: bool = False,
        xx: bool = False,
        gt: bool = False,
        lt: bool = False,
    ) -> bool: ...
    async def expireat(
        self,
        key: str,
        unix_time_seconds: Union[int, datetime.datetime],
        nx: bool = False,
        xx: bool = False,
        gt: bool = False,
        lt: bool = False,
    ) -> bool: ...
    async def keys(self, pattern: str) -> List[str]: ...
    async def persist(self, key: str) -> bool: ...
    async def pexpire(
        self,
        key: str,
        milliseconds: Union[int, datetime.timedelta],
        nx: bool = False,
        xx: bool = False,
        gt: bool = False,
        lt: bool = False,
    ) -> bool: ...
    async def pexpireat(
        self,
        key: str,
        unix_time_milliseconds: Union[int, datetime.datetime],
        nx: bool = False,
        xx: bool = False,
        gt: bool = False,
        lt: bool = False,
    ) -> bool: ...
    async def pttl(self, key: str) -> int: ...
    async def randomkey(self) -> Optional[str]: ...
    async def rename(self, key: str, newkey: str) -> bool: ...
    async def renamenx(self, key: str, newkey: str) -> bool: ...
    async def scan(
        self,
        cursor: int,
        match: Optional[str] = None,
        count: Optional[int] = None,
        type: Optional[str] = None,
    ) -> Tuple[int, List[str]]: ...
    async def touch(self, *keys: str) -> int: ...
    async def ttl(self, key: str) -> int: ...
    async def type(self, key: str) -> Optional[str]: ...
    async def unlink(self, *keys: str) -> int: ...
    async def geoadd(
        self,
        key: str,
        *members: Tuple[float, float, str],
        nx: bool = False,
        xx: bool = False,
        ch: bool = False,
    ) -> int: ...
    async def geodist(
        self,
        key: str,
        member1: str,
        member2: str,
        unit: Literal["M", "KM", "FT", "MI"] = "M",
    ) -> Optional[float]: ...
    async def geohash(self, key: str, *members: str) -> List[Optional[str]]: ...
    async def geopos(
        self, key: str, *members: str
    ) -> List[Union[Tuple[float, float], None]]: ...
    async def georadius(
        self,
        key: str,
        longitude: float,
        latitude: float,
        radius: float,
        unit: Literal["M", "KM", "FT", "MI"],
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
        count: Optional[int] = None,
        any: bool = False,
        order: Optional[Literal["ASC", "DESC"]] = None,
        store: Optional[str] = None,
        storedist: Optional[str] = None,
    ) -> Union[List[Union[str, GeoSearchResult]], int]: ...
    async def georadius_ro(
        self,
        key: str,
        longitude: float,
        latitude: float,
        radius: float,
        unit: Literal["M", "KM", "FT", "MI"],
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
        count: Optional[int] = None,
        any: bool = False,
        order: Optional[Literal["ASC", "DESC"]] = None,
    ) -> List[Union[str, GeoSearchResult]]: ...
    async def georadiusbymember(
        self,
        key: str,
        member: str,
        radius: float,
        unit: Literal["M", "KM", "FT", "MI"],
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
        count: Optional[int] = None,
        any: bool = False,
        order: Optional[Literal["ASC", "DESC"]] = None,
        store: Optional[str] = None,
        storedist: Optional[str] = None,
    ) -> Union[List[Union[str, GeoSearchResult]], int]: ...
    async def georadiusbymember_ro(
        self,
        key: str,
        member: str,
        radius: float,
        unit: Literal["M", "KM", "FT", "MI"],
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
        count: Optional[int] = None,
        any: bool = False,
        order: Optional[Literal["ASC", "DESC"]] = None,
    ) -> List[Union[str, GeoSearchResult]]: ...
    async def geosearch(
        self,
        key: str,
        unit: Literal["M", "KM", "FT", "MI"],
        member: Optional[str] = None,
        longitude: Optional[float] = None,
        latitude: Optional[float] = None,
        radius: Optional[float] = None,
        width: Optional[float] = None,
        height: Optional[float] = None,
        order: Optional[Literal["ASC", "DESC"]] = None,
        count: Optional[int] = None,
        any: bool = False,
        withdist: bool = False,
        withhash: bool = False,
        withcoord: bool = False,
    ) -> List[Union[str, GeoSearchResult]]: ...
    async def geosearchstore(
        self,
        destination: str,
        source: str,
        member: Optional[str] = None,
        longitude: Optional[float] = None,
        latitude: Optional[float] = None,
        unit: Literal["M", "KM", "FT", "MI"] = "M",
        radius: Optional[float] = None,
        width: Optional[float] = None,
        height: Optional[float] = None,
        order: Optional[Literal["ASC", "DESC"]] = None,
        count: Optional[int] = None,
        any: bool = False,
        storedist: bool = False,
    ) -> int: ...
    async def hdel(self, key: str, *fields: str) -> int: ...
    async def hexists(self, key: str, field: str) -> bool: ...
    async def hget(self, key: str, field: str) -> Optional[str]: ...
    async def hgetall(self, key: str) -> Dict[str, str]: ...
    async def hincrby(self, key: str, field: str, increment: int) -> int: ...
    async def hincrbyfloat(self, key: str, field: str, increment: float) -> float: ...
    async def hkeys(self, key: str) -> List[str]: ...
    async def hlen(self, key: str) -> int: ...
    async def hmget(self, key: str, *fields: str) -> List[Optional[str]]: ...
    async def hmset(self, key: str, values: Mapping[str, ValueT]) -> bool: ...
    async def hrandfield(
        self, key: str, count: Optional[int] = None, withvalues: bool = False
    ) -> Union[str, None, List[str], Dict[str, str]]: ...
    async def hscan(
        self,
        key: str,
        cursor: int,
        match: Optional[str] = None,
        count: Optional[int] = None,
    ) -> Tuple[int, Dict[str, str]]: ...
    async def hset(
        self,
        key: str,
        field: Optional[str] = None,
        value: Optional[ValueT] = None,
        values: Optional[Mapping[str, ValueT]] = None,
    ) -> int: ...
    async def hsetnx(self, key: str, field: str, value: ValueT) -> bool: ...
    async def hstrlen(self, key: str, field: str) -> int: ...
    async def hvals(self, key: str) -> List[str]: ...
    async def pfadd(self, key: str, *elements: ValueT) -> bool: ...
    async def pfcount(self, *keys: str) -> int: ...
    async def pfmerge(self, destkey: str, *sourcekeys: str) -> bool: ...
    async def lindex(self, key: str, index: int) -> Optional[str]: ...
    async def linsert(
        self,
        key: str,
        where: Literal["BEFORE", "AFTER"],
        pivot: ValueT,
        element: str,
    ) -> int: ...
    async def llen(self, key: str) -> int: ...
    async def lmove(
        self,
        source: str,
        destination: str,
        wherefrom: Literal["LEFT", "RIGHT"] = "LEFT",
        whereto: Literal["LEFT", "RIGHT"] = "RIGHT",
    ) -> Optional[str]: ...
    async def lpop(
        self, key: str, count: Optional[int] = None
    ) -> Union[str, List[str], None]: ...
    async def lpos(
        self,
        key: str,
        element: ValueT,
        rank: Optional[int] = None,
        count: Optional[int] = None,
        maxlen: Optional[int] = None,
    ) -> Union[(Optional[int]), List[int]]: ...
    async def lpush(self, key: str, *elements: ValueT) -> int: ...
    async def lpushx(self, key: str, *elements: ValueT) -> int: ...
    async def lrange(self, key: str, start: int, stop: int) -> List[str]: ...
    async def lrem(self, key: str, count: int, element: ValueT) -> int: ...
    async def lset(self, key: str, index: int, element: ValueT) -> bool: ...
    async def ltrim(self, key: str, start: int, stop: int) -> str: ...
    async def rpop(
        self, key: str, count: Optional[int] = None
    ) -> Union[str, List[str], None]: ...
    async def rpoplpush(self, source: str, destination: str) -> Optional[str]: ...
    async def rpush(self, key: str, *elements: ValueT) -> int: ...
    async def rpushx(self, key: str, *elements: ValueT) -> int: ...
    async def publish(self, channel: str, message: ValueT) -> int: ...
    async def eval(
        self,
        script: str,
        keys: Optional[List[str]] = None,
        args: Optional[List[str]] = None,
    ) -> Any: ...
    async def evalsha(
        self,
        sha1: str,
        keys: Optional[List[str]] = None,
        args: Optional[List[str]] = None,
    ) -> Any: ...
    async def dbsize(self) -> int: ...
    async def flushall(
        self, flush_type: Optional[Literal["ASYNC", "SYNC"]] = None
    ) -> bool: ...
    async def flushdb(
        self, flush_type: Optional[Literal["ASYNC", "SYNC"]] = None
    ) -> bool: ...
    async def time(self) -> Tuple[int, int]: ...
    async def sadd(self, key: str, *members: ValueT) -> int: ...
    async def scard(self, key: str) -> int: ...
    async def sdiff(self, *keys: str) -> List[str]: ...
    async def sdiffstore(self, destination: str, *keys: str) -> int: ...
    async def sinter(self, *keys: str) -> List[str]: ...
    async def sinterstore(self, destination: str, *keys: str) -> int: ...
    async def sismember(self, key: str, member: ValueT) -> bool: ...
    async def smismember(self, key: str, *members: ValueT) -> List[bool]: ...
    async def smembers(self, key: str) -> List[str]: ...
    async def smove(self, source: str, destination: str, member: ValueT) -> bool: ...
    async def spop(
        self, key: str, count: Optional[int] = None
    ) -> Union[str, List[str], None]: ...
    async def srandmember(
        self, key: str, count: Optional[int] = None
    ) -> Union[str, List[str], None]: ...
    async def srem(self, key: str, *members: ValueT) -> int: ...
    async def sscan(
        self,
        key: str,
        cursor: int = 0,
        match: Optional[str] = None,
        count: Optional[int] = None,
    ) -> Tuple[int, List[str]]: ...
    async def sunion(self, *keys: str) -> List[str]: ...
    async def sunionstore(self, destination: str, *keys: str) -> int: ...
    async def zadd(
        self,
        key: str,
        scores: Dict[str, float],
        nx: bool = False,
        xx: bool = False,
        gt: bool = False,
        lt: bool = False,
        ch: bool = False,
        incr: bool = False,
    ) -> Union[int, float, None]: ...
    async def zcard(self, key: str) -> int: ...
    async def zcount(self, key: str, min: FloatMinMaxT, max: FloatMinMaxT) -> int: ...
    async def zdiff(
        self, keys: List[str], withscores: bool = False
    ) -> Union[List[str], List[Tuple[str, float]]]: ...
    async def zdiffstore(self, destination: str, keys: List[str]) -> int: ...
    async def zincrby(self, key: str, increment: float, member: str) -> float: ...
    async def zinter(
        self,
        keys: List[str],
        weights: Union[List[float], List[int], None] = None,
        aggregate: Optional[Literal["SUM", "MIN", "MAX"]] = None,
        withscores: bool = False,
    ) -> Union[List[str], List[Tuple[str, float]]]: ...
    async def zinterstore(
        self,
        destination: str,
        keys: List[str],
        weights: Union[List[float], List[int], None] = None,
        aggregate: Optional[Literal["SUM", "MIN", "MAX"]] = None,
    ) -> int: ...
    async def zlexcount(self, key: str, min: str, max: str) -> int: ...
    async def zmscore(self, key: str, members: List[str]) -> List[Optional[float]]: ...
    async def zpopmax(
        self, key: str, count: Optional[int] = None
    ) -> List[Tuple[str, float]]: ...
    async def zpopmin(
        self, key: str, count: Optional[int] = None
    ) -> List[Tuple[str, float]]: ...
    async def zrandmember(
        self, key: str, count: Optional[int] = None, withscores: bool = False
    ) -> Union[str, None, List[str], List[Tuple[str, float]]]: ...
    async def zrange(
        self,
        key: str,
        start: FloatMinMaxT,
        stop: FloatMinMaxT,
        sortby: Optional[Literal["BYSCORE", "BYLEX"]] = None,
        rev: bool = False,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        withscores: bool = False,
    ) -> Union[List[str], List[Tuple[str, float]]]: ...
    async def zrangebylex(
        self,
        key: str,
        min: str,
        max: str,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> List[str]: ...
    async def zrangebyscore(
        self,
        key: str,
        min: FloatMinMaxT,
        max: FloatMinMaxT,
        withscores: bool = False,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> Union[List[str], List[Tuple[str, float]]]: ...
    async def zrangestore(
        self,
        dst: str,
        src: str,
        min: FloatMinMaxT,
        max: FloatMinMaxT,
        sortby: Optional[Literal["BYSCORE", "BYLEX"]] = None,
        rev: bool = False,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> int: ...
    async def zrank(self, key: str, member: str) -> Optional[int]: ...
    async def zrem(self, key: str, *members: str) -> int: ...
    async def zremrangebylex(self, key: str, min: str, max: str) -> int: ...
    async def zremrangebyrank(self, key: str, start: int, stop: int) -> int: ...
    async def zremrangebyscore(
        self, key: str, min: FloatMinMaxT, max: FloatMinMaxT
    ) -> int: ...
    async def zrevrange(
        self, key: str, start: int, stop: int, withscores: bool = False
    ) -> Union[List[str], List[Tuple[str, float]]]: ...
    async def zrevrangebylex(
        self,
        key: str,
        max: str,
        min: str,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> List[str]: ...
    async def zrevrangebyscore(
        self,
        key: str,
        max: FloatMinMaxT,
        min: FloatMinMaxT,
        withscores: bool = False,
        offset: Optional[int] = None,
        count: Optional[int] = None,
    ) -> Union[List[str], List[Tuple[str, float]]]: ...
    async def zrevrank(self, key: str, member: str) -> Optional[int]: ...
    async def zscan(
        self,
        key: str,
        cursor: int,
        match: Optional[str] = None,
        count: Optional[int] = None,
    ) -> Tuple[int, List[Tuple[str, float]]]: ...
    async def zscore(self, key: str, member: str) -> Optional[float]: ...
    async def zunion(
        self,
        keys: List[str],
        weights: Optional[List[float]] = None,
        aggregate: Optional[Literal["SUM", "MIN", "MAX"]] = None,
        withscores: bool = False,
    ) -> Union[List[str], List[Tuple[str, float]]]: ...
    async def zunionstore(
        self,
        destination: str,
        keys: List[str],
        weights: Optional[List[float]] = None,
        aggregate: Optional[Literal["SUM", "MIN", "MAX"]] = None,
    ) -> int: ...
    async def append(self, key: str, value: str) -> int: ...
    async def decr(self, key: str) -> int: ...
    async def decrby(self, key: str, decrement: int) -> int: ...
    async def get(self, key: str) -> Optional[str]: ...
    async def getdel(self, key: str) -> Optional[str]: ...
    async def getex(
        self,
        key: str,
        ex: Optional[int] = None,
        px: Optional[int] = None,
        exat: Optional[int] = None,
        pxat: Optional[int] = None,
        persist: Optional[bool] = None,
    ) -> Optional[str]: ...
    async def getrange(self, key: str, start: int, end: int) -> str: ...
    async def getset(self, key: str, value: ValueT) -> Optional[str]: ...
    async def incr(self, key: str) -> int: ...
    async def incrby(self, key: str, increment: int) -> int: ...
    async def incrbyfloat(self, key: str, increment: float) -> float: ...
    async def mget(self, *keys: str) -> List[Optional[str]]: ...
    async def mset(self, values: Mapping[str, ValueT]) -> Literal[True]: ...
    async def msetnx(self, values: Mapping[str, ValueT]) -> bool: ...
    async def psetex(
        self, key: str, milliseconds: int, value: str
    ) -> Literal[True]: ...
    async def set(
        self,
        key: str,
        value: ValueT,
        nx: bool = False,
        xx: bool = False,
        get: bool = False,
        ex: Optional[int] = None,
        px: Optional[int] = None,
        exat: Optional[int] = None,
        pxat: Optional[int] = None,
        keepttl: bool = False,
    ) -> Optional[str]: ...
    async def setex(self, key: str, seconds: int, value: ValueT) -> Literal[True]: ...
    async def setnx(self, key: str, value: ValueT) -> bool: ...
    async def setrange(self, key: str, offset: int, value: str) -> int: ...
    async def strlen(self, key: str) -> int: ...
    async def substr(self, key: str, start: int, end: int) -> str: ...
    async def script_exists(self, *sha1: str) -> List[bool]: ...
    async def script_flush(
        self, flush_type: Optional[Literal["ASYNC", "SYNC"]] = None
    ) -> bool: ...
    async def script_load(self, script: str) -> str: ...

class BitFieldCommands:
    def __init__(self, client: Commands, key: str): ...
    def get(self, encoding: str, offset: Union[int, str]) -> "BitFieldCommands": ...
    def set(
        self, encoding: str, offset: Union[int, str], value: int
    ) -> "BitFieldCommands": ...
    def incrby(
        self, encoding: str, offset: Union[int, str], increment: int
    ) -> "BitFieldCommands": ...
    def overflow(
        self, overflow: Literal["WRAP", "SAT", "FAIL"]
    ) -> "BitFieldCommands": ...
    def execute(self) -> List: ...

class BitFieldROCommands:
    def __init__(self, client: Commands, key: str): ...
    def get(self, encoding: str, offset: Union[int, str]) -> "BitFieldROCommands": ...
    def execute(self) -> List: ...

class AsyncBitFieldCommands:
    def __init__(self, client: AsyncCommands, key: str): ...
    def get(
        self, encoding: str, offset: Union[int, str]
    ) -> "AsyncBitFieldCommands": ...
    def set(
        self, encoding: str, offset: Union[int, str], value: int
    ) -> "AsyncBitFieldCommands": ...
    def incrby(
        self, encoding: str, offset: Union[int, str], increment: int
    ) -> "AsyncBitFieldCommands": ...
    def overflow(
        self, overflow: Literal["WRAP", "SAT", "FAIL"]
    ) -> "AsyncBitFieldCommands": ...
    async def execute(self) -> List: ...

class AsyncBitFieldROCommands:
    def __init__(self, client: AsyncCommands, key: str): ...
    def get(
        self, encoding: str, offset: Union[int, str]
    ) -> "AsyncBitFieldROCommands": ...
    async def execute(self) -> List: ...